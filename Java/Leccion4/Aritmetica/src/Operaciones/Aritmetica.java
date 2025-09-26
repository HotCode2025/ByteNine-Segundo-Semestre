/*CLASE 4:Tema: Clases y Objetos Poo parte 2 Tarea
Punto:4.6 Creación de Métodos
Vamos a crear la carpeta de la Lección 4*/
//Continuamos en classe 5
package Operaciones;

public class Aritmetica {

    //Atributos de la Clase
    int a;//Valor asignado por default 0
    int b;
// ..................------------------------------
//Clase 6A:Tema:Programacion orientada a objetos Parte 4
//Punto 6.1 Sobrecarga de metodos
//El constructor es un metodo especial
    public Aritmetica() { //Constructor 1(vacio)
        System.out.println("Se esta ejecuntando el constructor numero 1");
    }

    //estamos viendo lo que se llama sobrecarga de constructores
    public Aritmetica(int a, int b) { //Constructor 2
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando el constructor numero 2");
    }

    //Metodo (definirlo)vacio
    public void sumarNumeros() {
        int resultado = a + b;
        System.out.println("resultado = " +resultado);
    }

    /*Clase 5; Tema Clases y Objetos Parte 3 Tarea
     Punto: 5.2 Clase Aritmética: Creamos un método, recorremos con Debbug*/
    //Creamos otro metodo(retorna el valor de una expresion
    public int sumarConRetorno() {
        //int resultado = a + b;
        return a + b;

    }

    /*Punto: 5.3 Paso de argumentos a un método
    Creamos otro metodo*/
 /* public int sumarConArgumentos(int arg1, int arg2) {
        
        a = arg1;
        b = arg2;
        //return a + b;
        //Punto: 5.4 Un método llamando a otro método dentro de la misma classe.
        return sumarConRetorno();*/
    public int sumarConArgumentos(int a, int b){
        //Punto: 5.5 Operador this(uso opcional, se crea automaticamente)
        this.a = a;//El argumento a se asigna al atributo this.a
        this.b = b;
        //return a + b;
        //Punto: 5.4 Un método llamando a otro método dentro de la misma classe.
        return this.sumarConRetorno();

    }
}
