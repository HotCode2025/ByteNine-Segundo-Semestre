//Viene de Clase 4
/*Clase 5; Tema Clases y Objetos Parte 3 Tarea
Punto: 5.1 Clase Aritmética: Creamos un objeto*/
package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        //Creamos objeto
        Aritmetica aritmetica1 = new Aritmetica();//llamamos al constructor
        aritmetica1.a = 3;//llamamos a traves del objeto y colocamos valor
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();

        /*Clase 5; Tema Clases y Objetos Parte 3 Tarea
        Punto: 5.2 Clase Aritmética: Creamos un método, recorremos con Debbug*/
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
        
        
    }

}
