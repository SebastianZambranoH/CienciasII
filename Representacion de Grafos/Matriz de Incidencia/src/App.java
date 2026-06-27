import Control.ControladorGrafo;
import Modelo.ConstructorMatrizIncidencia;
import Modelo.IConstructorMatriz;
import Vista.VistaConsola;

public class App {
    public static void main(String[] args) {
        VistaConsola vista = new VistaConsola();
        IConstructorMatriz constructorMatriz = new ConstructorMatrizIncidencia();
        ControladorGrafo controlador = new ControladorGrafo(vista, constructorMatriz);
        controlador.iniciar();
    }
}
