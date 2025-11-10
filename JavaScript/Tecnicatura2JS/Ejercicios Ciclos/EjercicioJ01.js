//Ejercicio 01 Java a Js(ciclos)
//Leer un numero y mostrar su cuadrado.
// Repetir el proceso hasta que se introduzca un numero negativo.
//Simulamos que el usuario va ingresar numeros:
const numerosDeEntrada = [4, 7, 10, 0, 5, -5, 12, 1];


function calcularCuadrados() {
    
    // Usamos un ciclo FOR  para recorrer el array de entrada.
    // 'num' tomará el valor de cada elemento en 'numerosDeEntrada' secuencialmente.
    for (const num of numerosDeEntrada) {
        
        // 1. Condición de Parada (La lógica clave del ejercicio):
        if (num < 0) {
            console.log("El programa ha finalizado por número negativo.");
            break; // Detenemos el ciclo FOR 
        }

        //  Cálculo (Sólo si el número es >= 0)
        // 
        const cuadrado = num ** 2;

        // Mostramos el resultado.
        console.log(`El número ${num} elevado al cuadrado es: ${cuadrado}`);
    }

    
}

// Ejecutar el programa
calcularCuadrados();