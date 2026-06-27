package Modelo;

/**
 * Abstraccion para construir una matriz a partir de un Grafo.
 * El Controlador depende de esta interfaz, no de una implementacion concreta (DIP).
 * Si en el futuro se necesita, por ejemplo, una matriz de adyacencia,
 * basta con crear otra clase que la implemente, sin modificar el Controlador (OCP).
 */
public interface IConstructorMatriz {
    int[][] construir(Grafo grafo);
}
