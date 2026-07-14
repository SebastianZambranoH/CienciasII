# views/console_view.py

class ConsoleView:

    def show_menu(self):
        print("\n" + "=" * 60)
        print("      SISTEMA DE RESPUESTA A EMERGENCIAS")
        print("=" * 60)
        print("\nSeleccione una opcion:")
        print("1. Emergencia aleatoria")
        print("2. Elegir emergencia manualmente")

    def show_emergency_list(self, emergencies):
        print("\nEmergencias disponibles:\n")
        for i, emergency in enumerate(emergencies, 1):
            print(f"{i}. {emergency.get_name()}")

    def ask_option(self):
        return input("\nOpcion: ").strip()

    def ask_emergency_selection(self):
        return input("\nSeleccione una emergencia: ").strip()

    def show_station_analysis(self, stations):
        print("\n" + "=" * 60)
        print("          ANALISIS DE ESTACIONES")
        print("=" * 60)
        for station in stations:
            if station.get_response_time() > 0:
                print(f"\n{station.get_name()}")
                print(f"Tiempo: {station.get_response_time() / 60:.2f} minutos")
                print(f"Distancia: {station.get_distance() / 1000:.2f} km")

    def show_result(self, emergency, station):
        print("\n" + "=" * 60)
        print("        RESULTADO")
        print("=" * 60)
        print(f"\nEmergencia: {emergency.get_name()}")
        print(f"Estacion seleccionada: {station.get_name()}")
        print(f"Tiempo estimado: {station.get_response_time() / 60:.2f} minutos")
        print(f"Distancia: {station.get_distance() / 1000:.2f} km")
        print(f"Nodos recorridos: {len(station.get_route())}")

    def show_error(self, message):
        print(f"\n[ERROR] {message}")

    def show_message(self, message):
        print(f"\n{message}")