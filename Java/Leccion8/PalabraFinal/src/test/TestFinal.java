//10.4 Uso de la palabra reservada final, Parte 1 Y 2

/*
Uso de la palabra Final
Esta palabra tiene diferentes significados dependiendo donde se aplique
    Variables: Evitar cambiar el valor que almacena la variable.
    Metodos: Evita que se modifique la definicion de un metodo desde una 
             subclase (hija).
    Clases: Evita que se creen clases hijas.

Otras caracterisiticas es que normalmente, cuando trabajamos con variables
se cambian con el modificador de acceso estatico para convertir una
variable en una constante, es decir que no se puede modificar su valor,
el ejemplo de esto es la clase Math en lo cual sus atributos son de tipo
static y final, es por esto que la variable pi* se conoce como una constante.
*/
package test;

import domain.Persona;


public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 39555278;
        System.out.println("miDni = " + miDni);
        //miDni = 20312321 //No se puede modificar
        
//10.4 Uso de la palabra reservada final, Parte 3 y 4
        //Persona.CONSTANTE_AQUI = 9; //No se modifica
        System.out.println("Mi atributo constante es: " + Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona(); //10.4 Uso de la palabra reservada final, Parte 3 y 4
        //persona 1 = new Persona(); //No se puede asignar una nueva referencia
        persona1.setNombre("Ariel Bentancud");
        System.out.println("persona1 nombre: "+ persona1.getNombre());
        persona1.setNombre("Liliana");
        System.out.println("persona1 nombre: "+ persona1.getNombre());

        
    }
}
