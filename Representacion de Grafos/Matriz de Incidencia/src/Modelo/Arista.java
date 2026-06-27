package Modelo;

/**
 * Representa una arista (conexion) entre dos vertices de un grafo no dirigido.
 * Es un objeto inmutable: una vez creada, sus datos no cambian.
 */
public class Arista {

    private final char origen;
    private final char destino;
    private final int peso;

    public Arista(char origen, char destino, int peso) {
        this.origen = origen;
        this.destino = destino;
        this.peso = peso;
    }

    public char getOrigen() {
        return origen;
    }

    public char getDestino() {
        return destino;
    }

    public int getPeso() {
        return peso;
    }

    /**
     * Indica si la arista es un bucle (conecta un vertice consigo mismo).
     */
    public boolean esBucle() {
        return origen == destino;
    }

    @Override
    public String toString() {
        return origen + "-" + destino;
    }
}
