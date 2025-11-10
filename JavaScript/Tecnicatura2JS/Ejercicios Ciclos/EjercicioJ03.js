//Ejercicio 03 Java a Js(ciclos)
/*Ejercicio 3: Leer numeros hasta que se introduzca 0
 Para cada uno indicar si es par o impar
*/

// SIIMULAMOS LAS ENTRADAS DEL USUARIO
// Secuencia de NUMEROEl '0' detendrá el proceso.
const datosEntrada = [34, 29, 30, 55, 99, 18, 44, 108, 335, 543, 0]; 


function clasificarParImpar() {
    
    // Usamos el ciclo FOR para recorrer cada número del array de forma secuencial.
    for (const num of datosEntrada) {
        
        // simulamos que se ingreso 0 (esta en el ultimo lugar )
        if (num === 0) {
            console.log("---------------------------------------");
            console.log("Proceso finalizado: Se ha introducido el número cero.");
            break; // detenemos el ciclo 
        }

        // 
        // verificamos si el residuo de dividir el número por 2 es 0.
        if (num % 2 === 0) {
            console.log(`El número ${num} es PAR.`);
        } else {
            console.log(`El número ${num} es IMPAR.`);
        }
    }
}

clasificarParImpar();// Ejecutamos  el programa
