package Clase3;

import java.util.Scanner;

import javax.swing.JOptionPane;

public class Ejercicio5Ciclo {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int numero, numaleatorio, contador = 0;

        /*numaleatorio = (int)(Math.random() * 100); // Esto genera un numero aleatorio de 0 a 100

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
        System.out.println("\tAdivinaste el numero en " + contador + " intentos");
        */
        entrada.close();

        numaleatorio = (int)(Math.random() * 100);

        do{
            String num = JOptionPane.showInputDialog("Digite un numero: ");
            numero = Integer.parseInt(num);
            if(numero < numaleatorio){
                JOptionPane.showMessageDialog(null, "Digite un numero mayor");
                numero = Integer.parseInt(num);
            }
            else if (numero > numaleatorio){
                JOptionPane.showMessageDialog(null, "Ingrese un numero menor");
                numero = Integer.parseInt(num);
            }
            else{
                JOptionPane.showMessageDialog(null, "\t!!FELICIDADES¡¡ Hacertaste el numero");
            }
            contador++;
        }
        while(numero != numaleatorio);
        JOptionPane.showMessageDialog(null, "\tAdivinaste el numero en " + contador + " intentos");
    }
}
