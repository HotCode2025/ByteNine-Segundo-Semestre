/*CLASE 4:Clases y Objetos Poo parte 2 Tarea
4.2 Creacion de un Objeto(ViDEO 2)
4.3 Creacion de un objeto mas*/

package Clases;

public class PruebaPersona {

    public static void main(String[] args) {

        Persona persona1 = new Persona(); //Llamamos al constructor
        persona1.nombre = "Ariel"; //El valor hexadecimal normalmente comienza con 0x
        persona1.apellido = "Betancud";
        persona1.obtenerInformacion();

        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();
        persona2.nombre = "Osvaldo";
        persona2.apellido = "Giordanini";
        persona2.obtenerInformacion();
    }

}
