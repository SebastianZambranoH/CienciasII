# views/map_view.py

import folium
import osmnx as ox


class MapView:

    def __init__(self, graph, edges):
        self._graph = graph
        self._edges = edges

    def build_interactive_map(self, points_of_interest, station, emergency, route):
        lat, lon = (4.726734023564359, -74.04575503796416)
        map_ = folium.Map(location=[lat, lon], zoom_start=15, tiles="openstreetmap")

        self._draw_traffic_layer(map_)
        self._draw_markers(map_, points_of_interest)
        self._draw_route(map_, route)
        self._highlight_station(map_, station)
        self._highlight_emergency(map_, emergency)

        return map_

    def _draw_traffic_layer(self, map_):
        for _, row in self._edges.iterrows():
            if row['geometry'].geom_type == 'LineString':
                coords = [(lat, lon) for lon, lat in row['geometry'].coords]
                speed = row.get('speed_kph', 30)
                color = self._traffic_color(speed)

                folium.PolyLine(
                    locations=coords,
                    color=color,
                    weight=3.5,
                    opacity=0.8,
                    popup=f"Calle: {row.get('name', 'Sin nombre')}<br>Velocidad: {speed:.1f} km/h"
                ).add_to(map_)

    def _draw_markers(self, map_, points_of_interest):
        icons = {
            "station":   ("darkblue",  "shield",               "fa"),
            "hospital":  ("lightred",  "hospital",             "fa"),
            "emergency": ("darkred",   "exclamation-triangle", "fa"),
            "ambulance": ("orange",    "ambulance",            "fa"),
            "patrol":    ("darkgreen", "car",                  "fa"),
        }

        for location in points_of_interest:
            node = location.get_node()
            lat = self._graph.nodes[node]["y"]
            lon = self._graph.nodes[node]["x"]
            tipo = location.__class__.__name__.lower()
            color, icon, prefix = icons.get(tipo, ("blue", "map-marker", "fa"))

            folium.Marker(
                location=[lat, lon],
                popup=f"<b>{location.get_name()}</b>",
                icon=folium.Icon(color=color, icon=icon, prefix=prefix)
            ).add_to(map_)

    def _draw_route(self, map_, route):
        coords = [(self._graph.nodes[n]["y"], self._graph.nodes[n]["x"]) for n in route]
        folium.PolyLine(
            locations=coords,
            color="blue",
            weight=7,
            opacity=0.9,
            tooltip="Ruta optima A*"
        ).add_to(map_)

    def _highlight_station(self, map_, station):
        node = station.get_node()
        folium.CircleMarker(
            location=(self._graph.nodes[node]["y"], self._graph.nodes[node]["x"]),
            radius=10,
            color="green",
            fill=True,
            fill_color="green",
            popup="Estacion seleccionada"
        ).add_to(map_)

    def _highlight_emergency(self, map_, emergency):
        node = emergency.get_node()
        folium.CircleMarker(
            location=(self._graph.nodes[node]["y"], self._graph.nodes[node]["x"]),
            radius=10,
            color="red",
            fill=True,
            fill_color="red",
            popup="Emergencia"
        ).add_to(map_)

    def _traffic_color(self, speed):
        if speed <= 16:
            return '#E74C3C'
        elif speed <= 26:
            return '#F1C40F'
        return '#2ECC71'

    def save_interactive_map(self, map_, filename="mapa_emergencias.html"):
        map_.save(filename)
        print(f"Mapa guardado como '{filename}'")

    def build_static_map(self, points_of_interest):
        node_colors = []
        node_sizes = []

        color_map = {
            "station":   ("#00008B", 100),
            "hospital":   ("#FF474C", 100),
            "emergency": ("#8B0000", 110),
            "ambulance": ("#F39C12", 80),
            "patrol":   ("#006400", 80),
        }

        poi_nodes = {loc.get_node(): loc.__class__.__name__.lower()
                     for loc in points_of_interest}

        for node in self._graph.nodes():
            if node in poi_nodes:
                color, size = color_map.get(poi_nodes[node], ("#BDC3C7", 15))
            else:
                color, size = "#BDC3C7", 15
            node_colors.append(color)
            node_sizes.append(size)

        edge_colors, edge_widths = self._get_edge_styles()

        return self._graph, node_colors, node_sizes, edge_colors, edge_widths

    def _get_edge_styles(self):
        colors, widths = [], []
        for _, _, _, data in self._graph.edges(keys=True, data=True):
            speed = data.get('speed_kph', 30)
            if speed <= 16:
                colors.append('#E74C3C'); widths.append(2.5)
            elif speed <= 26:
                colors.append('#F1C40F'); widths.append(1.8)
            else:
                colors.append('#2ECC71'); widths.append(1.2)
        return colors, widths

    def save_static_map(self, all_locations, filename="grafo_trafico.png"):
        graph, node_colors, node_sizes, edge_colors, edge_widths = self.build_static_map(all_locations)
        fig, ax = ox.plot_graph(
            graph,
            node_color=node_colors,
            node_size=node_sizes,
            edge_color=edge_colors,
            edge_linewidth=edge_widths,
            bgcolor='#1A252F',
            show=True,
            close=False
        )
        fig.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Grafo guardado como '{filename}'")