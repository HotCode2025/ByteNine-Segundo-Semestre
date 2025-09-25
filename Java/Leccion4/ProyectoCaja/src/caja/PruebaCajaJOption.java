package caja;

import javax.swing.JOptionPane;

/**
 *
 * @author garod
 */
public class PruebaCajaJOption {
    public static void main(String[] args) {
        // Pedimos valores al ususario con JoptionPane

        double ancho = Double.parseDouble(
                JOptionPane.showInputDialog("Ingrese el ancho de la caja: "));

        double alto = Double.parseDouble(
                JOptionPane.showInputDialog("Ingrese el alto de la caja: "));

        double profundidad = Double.parseDouble(
                JOptionPane.showInputDialog("Ingrese la profundidad de la caja: "));

        // Creamos el objeto
        Caja caja1 = new Caja(ancho, alto, profundidad);

        // Calculamos volumen
        double volumen = caja1.calcularVolumen();

        // Mostramos lo resultados
        JOptionPane.showMessageDialog(null, "El volumen de la caja es: " + volumen);
    }
    
}
