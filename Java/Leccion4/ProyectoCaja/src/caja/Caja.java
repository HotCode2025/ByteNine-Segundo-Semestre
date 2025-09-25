package caja;

/**
 *
 * @author garod
 */
public class Caja {

    // atributos
    double ancho;
    double alto;
    double profundidad;

    // constructor vacio
    public Caja() {
    }

    // constructor con los parámetros
    public Caja(double ancho, double alto, double profundidad) {
        this.ancho = ancho;
        this.alto = alto;
        this.profundidad = profundidad;

    }

    // Metodo para calcular el volumen
    public double calcularVolumen() {
        return ancho * alto * profundidad;
    }

}
