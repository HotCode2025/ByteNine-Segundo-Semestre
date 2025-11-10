//Ejercicio 06 Java a Js(ciclos)
/*Ejercicio 6: Pedir numeros hasta que se tecle un 0, 
mostrar la suma de todos los numeros introducidos*/

// Simulamos la entrada de ingreso de numeros
// Secuencia de números a sumar. El '0' detendrá el proceso.
const datosEntrada = [10, 5, 68, -2, 1, -45, 23, 89, 71, 0]; 


function sumarNumeros() {
    
    let suma = 0; //la variable que va acumular los numeros, inicilizamos en 0
    //recorremos con el ingreso de los numeros con for
    for (const num of datosEntrada) {
        
        // 1. Condición de Parada:
        if (num === 0) {
            console.log("---------------------------------------");
            console.log("Proceso finalizado: Se ha introducido el cero.");
            break; // Detenemos el ciclo FOR cuando se ingrese el cero(esta al ultimo).
        }

        // Acumulación:
        // sumamos el número actual al total de la suma.
        suma += num; 
        
        console.log(`Sumando: ${num}. Suma actual: ${suma}`);
    }

    // Mostramos los resultados
    console.log("---------------------------------------");
    console.log(`La suma total de los números introducidos es: ${suma}`);
}

// Ejecutar el programa
sumarNumeros();