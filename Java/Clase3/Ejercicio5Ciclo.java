package Clase3;

import java.util.Scanner;

public class Ejercicio5Ciclo {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int numero, numaleatorio, contador = 0;

        numaleatorio = (int)(Math.random() * 100); // Esto genera un numero aleatorio de 0 a 100

        do{
        System.out.println("Digite un numoer : ");
        numero = Integer.parseInt(entrada.nextLine());

        if (numero < numaleatorio){
            System.out.println("Digite un numero mayor");
        }
        else if (numero > numaleatorio){
            System.out.println("Ingrese un numero menor");
        }
        else{
            System.out.println("\t!!FELICIDADES¡¡ Hacertaste el numero");
        }
        contador++;

    }while(numero != numaleatorio);
    entrada.close();
    System.out.println("\tAdivinaste el numero en " + contador + " intentos");
    
    }
}
