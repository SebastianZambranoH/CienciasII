package sendingemail;

public class Arista {

    private int destino;
    private int peso;

    // Constructor de la arista
    public Arista(int destino, int peso) {
        this.destino = destino;
        this.peso = peso;
    }

    public int getDestino() {
        return destino;
    }

    public int getPeso() {
        return peso;
    }

    public void setDestino(int destino) {
        this.destino = destino;
    }

    public void setPeso(int peso) {
        this.peso = peso;
    }

}