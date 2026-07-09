package sendingemail;

import java.util.ArrayList;
import java.util.PriorityQueue;

public class Grafo {

    private ArrayList<ArrayList<Arista>> listaAdyacencia;
    private int numeroVertices;

    // Crea la lista de adyacencia
    public Grafo(int numeroVertices) {

        this.numeroVertices = numeroVertices;
        listaAdyacencia = new ArrayList<>();

        for (int i = 0; i < numeroVertices; i++) {
            listaAdyacencia.add(new ArrayList<>());
        }

    }

    // Agrega una conexión en ambos sentidos
    public void agregarArista(int origen, int destino, int peso) {

        listaAdyacencia.get(origen).add(new Arista(destino, peso));
        listaAdyacencia.get(destino).add(new Arista(origen, peso));

    }

    // Algoritmo de Dijkstra
    public int dijkstra(int origen, int destino) {

        int[] distancia = new int[numeroVertices];
        boolean[] visitado = new boolean[numeroVertices];

        // Inicializa las distancias
        for (int i = 0; i < numeroVertices; i++) {
            distancia[i] = Integer.MAX_VALUE;
            visitado[i] = false;
        }

        PriorityQueue<Nodo> cola = new PriorityQueue<>();

        distancia[origen] = 0;
        cola.offer(new Nodo(origen, 0));

        while (!cola.isEmpty()) {

            Nodo actual = cola.poll();
            int verticeActual = actual.getVertice();

            if (visitado[verticeActual]) {
                continue;
            }

            visitado[verticeActual] = true;

            // Si llega al destino termina
            if (verticeActual == destino) {
                return distancia[destino];
            }

            // Recorre los vecinos del nodo actual
            for (Arista arista : listaAdyacencia.get(verticeActual)) {

                int vecino = arista.getDestino();
                int peso = arista.getPeso();

                // Actualiza la distancia si encuentra un camino mejor
                if (!visitado[vecino]
                        && distancia[verticeActual] + peso < distancia[vecino]) {

                    distancia[vecino] = distancia[verticeActual] + peso;

                    cola.offer(new Nodo(vecino, distancia[vecino]));

                }

            }

        }

        // No existe un camino al destino
        return -1;

    }

}