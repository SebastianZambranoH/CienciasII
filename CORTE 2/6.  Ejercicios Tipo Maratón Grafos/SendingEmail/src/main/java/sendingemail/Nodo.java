package sendingemail;

public class Nodo implements Comparable<Nodo> {

    private int vertice;
    private int distancia;

    // Constructor del nodo
    public Nodo(int vertice, int distancia) {
        this.vertice = vertice;
        this.distancia = distancia;
    }

    public int getVertice() {
        return vertice;
    }

    public int getDistancia() {
        return distancia;
    }

    public void setVertice(int vertice) {
        this.vertice = vertice;
    }

    public void setDistancia(int distancia) {
        this.distancia = distancia;
    }

    // Ordena los nodos por distancia
    @Override
    public int compareTo(Nodo otro) {
        return Integer.compare(this.distancia, otro.distancia);
    }

}