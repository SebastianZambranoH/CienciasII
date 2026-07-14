# controllers/emergency_controller.py

import random
from algorithms.astar import AStar


class EmergencyController:

    def __init__(self, graph):
        self._graph = graph
        self._astar = AStar()

    def select_emergency(self, emergencies, choice):
        if choice == "random":
            return random.choice(emergencies)
        return emergencies[choice]

    def find_best_station(self, stations, emergency):
        best_station = None
        best_route = None
        best_time = float("inf")

        for station in stations:
            try:
                route, time, distance = self._astar.calculate_route(
                    self._graph,
                    station.get_node(),
                    emergency.get_node()
                )

                if time < best_time:
                    best_time = time
                    best_station = station
                    best_route = route

                    station.set_response_time(time)
                    station.set_distance(distance)
                    station.set_route(route)

            except Exception:
                continue

        return best_station, best_route

    def get_route_details(self, station):
        return {
            "tiempo": station.get_response_time(),
            "distancia": station.get_distance(),
            "ruta": station.get_route()
        }