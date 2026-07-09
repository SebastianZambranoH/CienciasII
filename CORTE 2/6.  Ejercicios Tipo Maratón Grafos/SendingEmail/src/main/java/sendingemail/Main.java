package sendingemail;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // Lee la cantidad de casos
        int casos = scanner.nextInt();

        for (int i = 1; i <= casos; i++) {

            int n = scanner.nextInt();
            int m = scanner.nextInt();
            int origen = scanner.nextInt();
            int destino = scanner.nextInt();

            Grafo grafo = new Grafo(n);

            // Lee todas las conexiones
            for (int j = 0; j < m; j++) {

                int u = scanner.nextInt();
                int v = scanner.nextInt();
                int peso = scanner.nextInt();

                grafo.agregarArista(u, v, peso);

            }

            // Ejecuta Dijkstra
            int respuesta = grafo.dijkstra(origen, destino);

            if (respuesta == -1) {
                System.out.println("Case #" + i + ": unreachable");
            } else {
                System.out.println("Case #" + i + ": " + respuesta);
            }

        }

        scanner.close();

    }

}