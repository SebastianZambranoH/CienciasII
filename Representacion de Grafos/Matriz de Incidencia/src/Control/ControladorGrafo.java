package Control;

import Modelo.*;
import Vista.VistaConsola;
/**
 * Controlador: dirige el flujo de la aplicacion.
 * No sabe COMO se lee/escribe (eso es de VistaConsola)
 * ni COMO se construye la matriz (eso es de IConstructorMatriz).
 * Solo coordina.
 */
public class ControladorGrafo {

    private final VistaConsola vista;
    private final IConstructorMatriz constructorMatriz;
    private Grafo grafo;

    public ControladorGrafo(VistaConsola vista, IConstructorMatriz constructorMatriz) {
        this.vista = vista;
        this.constructorMatriz = constructorMatriz;
    }

    public void iniciar() {
        int numVertices = vista.solicitarNumeroVertices();
        this.grafo = new Grafo(numVertices);

        char[] vertices = grafo.getVertices();
        for (int i = 0; i < vertices.length; i++) {
            for (int j = i + 1; j < vertices.length; j++) {
                char origen = vertices[i];
                char destino = vertices[j];
                int peso = vista.solicitarPeso(origen, destino);
                if (peso != 0) {
                    grafo.agregarArista(new Arista(origen, destino, peso));
                }
            }
        }

        int[][] matriz = constructorMatriz.construir(grafo);
        vista.mostrarMatrizIncidencia(grafo, matriz);
        vista.cerrar();
    }
}
