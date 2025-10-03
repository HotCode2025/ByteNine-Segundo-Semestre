//8.6 Contexto estatico practica Parte 2 Ejecutar con debug File
package test;

import domain.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona ("Ariel");
        System.out.println("persona1 = " + persona1);
        Persona persona2 = new Persona ("Naty");
        System.out.println("persona2 = " + persona2);
    }
}
