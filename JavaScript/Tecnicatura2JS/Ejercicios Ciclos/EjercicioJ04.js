//Ejercicio 04 Java a Js(ciclos)
 /*Ejercicio 4: Pedir numeros hasta que se teclee uno negativo,
  *mostrar Cuantos numeros se han introducido.*/

 // Simulamos la entrada de datos
// Secuencia de números a analizar. El primer número negativo (-40) detendrá el proceso.
const numIngresados = [15, 8, 0, 10, 5, 45, 7, -40, 21, 3]; 

function contarPositivosYCeros() {
    
    // Variables de control de la entrada
    let i = 0; // Índice para leer el array
    let num = numIngresados[i]; // Primer número
    
    // Variables para el resultado del ejercicio
    let contador = 0; // Contador de números
    const numerosIntroducidosValidos = []; //array para almacenar los números válidos

    // El ciclo continúa mientras el número actual sea positivo o cero y no hayamos terminado el array.
    while (num >= 0 && i < numIngresados.length) {
        
        // 1. Almacenamos el número actual en el nuevo array.
        numerosIntroducidosValidos.push(num); 
        
        // 2. Contamos el número.
        contador++;
        
        // 3. Avanzamos al siguiente número en el array.
        i++; 
        num = numIngresados[i]; 
    }

    // El ciclo termina.
    console.log("---------------------------------------");
    console.log(`Proceso finalizado. El número negativo (${numIngresados[i]}) finalizo el programa.`);
    console.log(`Se han introducido ${contador} números.`);
    
    // Mostramos la lista completa de números almacenados.
    console.log(`Los números ingresados correctamente fueron: ${numerosIntroducidosValidos.join(', ')}`);
}

// Ejecutar el programa
contarPositivosYCeros();