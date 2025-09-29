//Viene de Clase 4
/*Clase 5; Tema Clases y Objetos Parte 3 Tarea
Punto: 5.1 Clase Aritmética: Creamos un objeto*/
package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        var a = 10; //Variables locales
        int b = 7;  //Memoria Stack
        miMetodo(); //Llamamos el método nuevo
        //Creamos objeto
        Aritmetica aritmetica1 = new Aritmetica();//llamamos al constructor
        aritmetica1.a = 3;//llamamos a traves del objeto y colocamos valor
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();

        /*Clase 5; Tema Clases y Objetos Parte 3 Tarea
        Punto: 5.2 Clase Aritmética: Creamos un método, recorremos con Debbug*/
        //Para almacenar un objeto o atributos se utiliza la memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " +resultado);

        //Punto:5.3 Paso de argumentos a un método
        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = " +resultado);

        //Clase 6A:Tema:Programacion orientada a objetos Parte 4
        //Punto 6.1 Sobrecarga de metodos
        System.out.println("aritmetica1  a:  "+aritmetica1.a);
        System.out.println("aritmetica1  b:  "+aritmetica1.b);
       
        Aritmetica arimetica2 = new Aritmetica(5,8);
        System.out.println("arimetica2 = " + arimetica2.a);
        System.out.println("arimetica2 = " + arimetica2.b);
        //aritmetica1 = null; Nunca utilizar esto, no debe hacerse
        //System.gc(); Metodo para limpiar residuos, es pasado, no utilizar
        //Punto: 7.1 Uso de la palabra this Parte 1 y crear una clase a continuacion de otra
        Persona persona = new Persona("Ariel", "Betancud");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: "+ persona.nombre);
        System.out.println("Persona apellido: "+ persona.apellido);
        
    }
    //Modularidad  creamos un nuevo metodo
    public static void miMetodo(){
        //a = 10; //ima variable esta limitada
        System.out.println("Aqui hay otro método");
    }

}
//Clase 6B: Tema: Programacion orientada a objetos Parte 5-Tarea
//Punto: 7.1 Uso de la palabra this Parte 1 y crear una clase a continuacion de otra
//Creamos una nueva clase
class Persona{
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido){//Constructor
        super();//Llamada al constructor de la clase Padre object
        this.nombre = nombre;
        this.apellido = apellido;
        //Punto7.4 uso de la palabra this parte 2
        System.out.println("Objeto persona usando this: "+ this);
    }

}
class Imprimir{
    public Imprimir (){
        super(); //El constructor de la clase padre, para reservar memoria
    }
    
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresion del objeto actual (this): "+this);
    }
}
