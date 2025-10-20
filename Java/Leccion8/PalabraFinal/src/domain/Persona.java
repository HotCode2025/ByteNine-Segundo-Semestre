//10.4 Uso de la palabra reservada final, Parte 1 y 2
package domain;

public class Persona {
    public final static int CONSTANTE_AQUI = 15; //10.4 Uso de la palabra reservada final, Parte 3 y 4
    private String nombre;

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    public void imprimir(){
        System.out.println("Metodo para imprimir");
    }
}
