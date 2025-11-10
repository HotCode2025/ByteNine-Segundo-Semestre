/*Clase 5; Tema Clases y Objetos Parte 3 Tarea
Punto: 5.8 Ejercicio Ciclos 09 con Scanner y JOptionPane*/
/*Ejercicio 9: Pedir el dia, mes y año de una fecha e indicar 
si la fecha es correcta. suponiendo que todos los meses
son de 30 dias*/
//Clase Scanner
package Ciclos09;

import java.util.Scanner;

public class Ciclos09 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.print("Ingrese el día: ");
        int dia = entrada.nextInt();

        System.out.print("Ingrese el mes: ");
        int mes = entrada.nextInt();

        System.out.print("Ingrese el año: ");
        int anio = entrada.nextInt();

        if ((dia >= 1 && dia <= 30) && (mes >= 1 && mes <= 12) && (anio > 0)) {
            System.out.println("La fecha " + dia + "/" + mes + "/" + anio + " es correcta.");
        } else {
            System.out.println("La fecha " + dia + "/" + mes + "/" + anio + " es incorrecta.");
        }

        entrada.close();
    }
    
}
