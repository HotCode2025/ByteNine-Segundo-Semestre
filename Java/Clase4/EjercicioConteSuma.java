package Ciclos06;

import java.util.Scanner;

public class Ciclos {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        int suma = 0;
        System.out.println("Ingrese números, cuando ingrese 0 sale del programa");

        do {
            numero = entrada.nextInt();
            suma += numero;
        } while (numero != 0);

        System.out.println("La suma de todos los números es: " + suma);
    }
}
