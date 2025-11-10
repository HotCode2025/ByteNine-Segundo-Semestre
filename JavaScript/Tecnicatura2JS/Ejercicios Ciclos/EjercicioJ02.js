//Ejercicio 02 Java a Js(ciclos)
/*Ejercicio2: Leer un numero e indicar si es positivo o negativo.
El proceso se repetira hasta que se introduzca un  cero 0. */

//Simulamos la introduccion de datos
// El '0' detendrá el proceso.
const datosEntrada = [30, -5, 8, -20, 25, 50, -100, 78, 0, -40, 55]; 


function positivoONegativo() {
    
    // Usamos un ciclo FOR para recorrer cada numero en el array.
    for (const num of datosEntrada) {
        
        // establecemos la condicion  si se introduce cero finaliza
        if (num === 0) {
            console.log("---------------------------------------");
            console.log("Proceso finalizado: Se ha introducido un cero.");
            break; // se detiene
        }
         //Solo si el número NO es cero
        if (num > 0) {
            console.log(`El número ${num} es: POSITIVO.`);
        } else { 
            console.log(`El número ${num} es: NEGATIVO.`);
        }
    }
}

// Ejecutar el programa
positivoONegativo();
