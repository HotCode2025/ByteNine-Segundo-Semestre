
package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57.000, false);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());

        //Modificar a traves de los metodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio"; //Ya no se puede utilizar
        //System.out.println("Nombre es: "+persona1.nombre); //Error
        System.out.println("persona1 con su nombre modificado es: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el booleano: "+persona1.isEliminado());
        
        //Tarea
        
        //Creamos otro objeto tipo Persona
        Persona persona2 = new Persona("Gustavo", 1, true);
        
        //Imprimimos sus valores iniciales
        System.out.println("persona2 su nombre es: "+persona2.getNombre());
        System.out.println("persona2 su salario es: "+persona2.getSueldo());
        System.out.println("persona2 para obtener el booleano: "+persona2.isEliminado());
        
        //Modificamos valores iniciales
        persona2.setNombre("Agustin Santarena");
        persona2.setSueldo(100);
        persona2.setEliminado(false);
        
        //Imprimimos valores modificados
        System.out.println("persona2 nombre modificado es: "+persona2.getNombre());
        System.out.println("persona2 sueldo modificado es: "+persona2.getSueldo());
        System.out.println("persona2 booleano modificado es: "+persona2.isEliminado());
    }
}
