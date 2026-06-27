package Vista;

import java.util.List;
import java.util.Scanner;
import Modelo.*;

/**
 * Vista: toda la entrada/salida por consola vive aqui.
 * Ni el Modelo ni el Controlador imprimen ni leen directamente del Scanner.
 */
public class VistaConsola {

    private final Scanner scanner;

    public VistaConsola() {
        this.scanner = new Scanner(System.in);
    }

    public int solicitarNumeroVertices() {
        System.out.println("Ingrese el # de vertices");
        return scanner.nextInt();
    }

    public int solicitarPeso(char origen, char destino) {
        System.out.println("Ingrese el peso del vertice entre: " + origen + " y " + destino
                + ". Si no hay conexion pulse 0");
        return scanner.nextInt();
    }

    public void mostrarMatrizIncidencia(Grafo grafo, int[][] matriz) {
        List<Arista> aristas = grafo.getAristas();
        char[] vertices = grafo.getVertices();

        System.out.print("\t");
        for (Arista arista : aristas) {
            System.out.print(arista + "\t");
        }
        System.out.println("\n");

        for (int i = 0; i < vertices.length; i++) {
            System.out.print(vertices[i] + "\t");
            for (int j = 0; j < aristas.size(); j++) {
                System.out.print(matriz[i][j] + "\t");
            }
            System.out.println();
        }
    }

    public void cerrar() {
        scanner.close();
    }
}
