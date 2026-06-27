package Modelo;

/**
 * Construye la matriz de incidencia de un grafo no dirigido.
 * Filas = vertices, columnas = aristas.
 * Convencion usada:
 *   2 -> el vertice tiene un bucle en esa arista
 *   1 -> el vertice es extremo de esa arista
 *   0 -> el vertice no participa en esa arista
 */
public class ConstructorMatrizIncidencia implements IConstructorMatriz {

    @Override
    public int[][] construir(Grafo grafo) {
        int numVertices = grafo.getNumVertices();
        int numAristas = grafo.getAristas().size();
        int[][] matriz = new int[numVertices][numAristas];

        for (int k = 0; k < numAristas; k++) {
            Arista arista = grafo.getAristas().get(k);
            int filaOrigen = grafo.indiceDe(arista.getOrigen());
            int filaDestino = grafo.indiceDe(arista.getDestino());

            if (arista.esBucle()) {
                matriz[filaOrigen][k] = 2;
            } else {
                matriz[filaOrigen][k] = 1;
                matriz[filaDestino][k] = 1;
            }
        }
        return matriz;
    }
}
