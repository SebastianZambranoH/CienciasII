package Modelo;

import java.util.ArrayList;
import java.util.List;

/**
 * Modelo del grafo: almacena los vertices y las aristas.
 * No conoce nada de entrada/salida ni de como se construye la matriz;
 * eso es responsabilidad de la Vista y de IConstructorMatriz (SRP).
 */
public class Grafo {

    private static final String ABECEDARIO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    private final char[] vertices;
    private final List<Arista> aristas;

    public Grafo(int numVertices) {
        this.vertices = new char[numVertices];
        for (int i = 0; i < numVertices; i++) {
            this.vertices[i] = ABECEDARIO.charAt(i);
        }
        this.aristas = new ArrayList<>();
    }

    public void agregarArista(Arista arista) {
        this.aristas.add(arista);
    }

    public char[] getVertices() {
        return vertices;
    }

    public List<Arista> getAristas() {
        return aristas;
    }

    public int getNumVertices() {
        return vertices.length;
    }

    /**
     * Devuelve la posicion (fila) que ocupa un vertice dentro del arreglo.
     */
    public int indiceDe(char vertice) {
        for (int i = 0; i < vertices.length; i++) {
            if (vertices[i] == vertice) {
                return i;
            }
        }
        return -1;
    }
}
