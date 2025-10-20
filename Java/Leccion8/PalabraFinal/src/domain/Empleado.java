//10.4 Uso de la palabra reservada final, Parte 1 y 2
package domain;

public class Empleado extends Persona {
    
    @Override
    public void imprimir(){
        System.out.println("Metodo imprimir desde la clase hija");
    }
}
