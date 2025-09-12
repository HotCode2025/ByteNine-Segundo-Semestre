// Maxi
// Calcular la suma de N Terminos de la siguiente serie:
// S = 1 - 1/2 + 1/3 - 1/4 + 1/5 - 1/6 ... 1/N


let n = 7; // Elegimos el valor, ya sea ej1: 2, 4, 6, 8, 10, 20, 30... (puede ser numero par o impar ej2: 1, 3, 5 o 2, 4, 6
let suma = 0; // Cuando iniciamos, esta guarda y almacena el resultado de la serie
let signo = 1; // Aca verifica si el numero es positivo o negativo
let i = 1; // El contador va a recorrer los numeros de la sirie, ej: 1, 2, 3, 4...

while (i <= n){ // El bucle comienza a ejecutar mientras i sea menor o igual a n
  suma = suma + signo / i; // Segun el signo se suma o resta el termino
  signo = signo * - 1; // Se cambia el signo en lo cual si llega ser 1, lo pasa a -1 // Y si es -1, lo pasa a 1
  i = i + 1; // Se le suma 1 a "i" para ir al siguiente numero
}

console.log("el resultado es: " + suma); // Se muestra un resultado final del valor que ingresamos