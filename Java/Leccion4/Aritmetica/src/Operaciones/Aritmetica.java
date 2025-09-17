/*CLASE 4:Tema: Clases y Objetos Poo parte 2 Tarea
Punto:4.6 Creación de Métodos
Vamos a crear la carpeta de la Lección 4*/
//Continuamos en classe 5
package Operaciones;

public class Aritmetica {

    //Atributos de la Clase
    int a;//Valor asignado por default 0
    int b;
// Como estan
    //Metodo (definirlo)vacio
    public void sumarNumeros() {
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }

    /*Clase 5; Tema Clases y Objetos Parte 3 Tarea
Punto: 5.2 Clase Aritmética: Creamos un método, recorremos con Debbug*/
    //Creamos otro metodo(retorna el valor de una expresion
    public int sumarConRetorno() {
        //int resultado = a + b;
        //return resultado;
        return this.a + this.b;
    }

    /*Punto: 5.3 Paso de argumentos a un método
    Creamos otro metodo*/
   /* public int sumarConArgumentos(int arg1, int arg2) {
        
        a = arg1;
        b = arg2;
        //return a + b;
        //Punto: 5.4 Un método llamando a otro método dentro de la misma classe.
        return sumarConRetorno();*/
    
    
      public int sumarConArgumentos(int a, int b) {
        //Punto: 5.5 Operador this(uso opcional, se crea automaticamente)
        this.a = b;//El argumento a se asigna al atributo this.a
        this.b = b;
        //return a + b;
        //Punto: 5.4 Un método llamando a otro método dentro de la misma classe.
        return this.sumarConRetorno();

    }
}
