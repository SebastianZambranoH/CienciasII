# controllers/app_controller.py

import random
from config.settings import (
    VERTICES, STATIONS_DATA, HOSPITALS_DATA, EMERGENCIES_DATA
)
from controllers.GraphController import GraphController
from controllers.EmergencyController import EmergencyController
from views.ConsoleView import ConsoleView
from views.MapView import MapView
from models.station import Station
from models.hospital import Hospital
from models.emergency import Emergency


class AppController:

    def __init__(self):
        self._console = ConsoleView()
        self._graph_controller = GraphController()
        self._stations = []
        self._hospitals = []
        self._emergencies = []
        self._graph_model = None
        self._emergency_controller = None
        self._map_view = None

    def run(self):
        self._setup()
        emergency = self._select_emergency()
        best_station, route = self._emergency_controller.find_best_station(
            self._stations, emergency
        )
        self._show_results(emergency, best_station)
        self._generate_maps(emergency, best_station, route)

    def _setup(self):
        self._console.show_message("Cargando mapa de Bogota...")
        self._build_locations()

        self._graph_model = self._graph_controller.build_graph(VERTICES)
        graph = self._graph_model.get_graph()

        self._graph_controller.assign_nodes_to_locations(self._stations, graph)
        self._graph_controller.assign_nodes_to_locations(self._hospitals, graph)

        occupied = [loc.get_node() for loc in self._stations + self._hospitals]
        self._graph_controller.assign_random_nodes(self._emergencies, graph, occupied)

        self._emergency_controller = EmergencyController(graph)
        self._map_view = MapView(graph, self._graph_model.get_edges())

    def _build_locations(self):
        for data in STATIONS_DATA:
            self._stations.append(Station(data["name"], data["lat"], data["lon"]))

        for data in HOSPITALS_DATA:
            self._hospitals.append(Hospital(data["name"], data["lat"], data["lon"]))

        for data in EMERGENCIES_DATA:
            self._emergencies.append(Emergency(data["name"], 0, 0))

    def _assign_random_nodes_to_emergencies(self, graph):
        occupied = [loc.get_node() for loc in self._stations + self._hospitals]
        available = [n for n in graph.nodes() if n not in occupied]

        for emergency in self._emergencies:
            node = random.choice(available)
            emergency.set_node(node)

    def _select_emergency(self):
        while True:
            self._console.show_menu()
            option = self._console.ask_option()

            if option == "1":
                return self._emergency_controller.select_emergency(
                    self._emergencies, "random"
                )

            elif option == "2":
                return self._select_manual_emergency()

            else:
                self._console.show_error("Opcion invalida.")

    def _select_manual_emergency(self):
        while True:
            self._console.show_emergency_list(self._emergencies)
            try:
                selection = int(self._console.ask_emergency_selection()) - 1
                if 0 <= selection < len(self._emergencies):
                    return self._emergency_controller.select_emergency(
                        self._emergencies, selection
                    )
                self._console.show_error("Seleccion fuera de rango.")
            except ValueError:
                self._console.show_error("Ingrese un numero valido.")

    def _show_results(self, emergency, best_station):
        self._console.show_station_analysis(self._stations)
        self._console.show_result(emergency, best_station)

    def _generate_maps(self, emergency, best_station, route):
        all_locations = self._stations + self._hospitals + self._emergencies
        interactive_map = self._map_view.build_interactive_map(
            all_locations, best_station, emergency, route
        )
        self._map_view.save_interactive_map(interactive_map)
        self._map_view.save_static_map(all_locations)