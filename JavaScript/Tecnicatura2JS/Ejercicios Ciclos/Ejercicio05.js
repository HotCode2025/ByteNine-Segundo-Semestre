//Ejercicio ciclos 05 de Pseint(Teoria Practica): 
// Calcular la siguiente sumatoria de N elementos:
//S= 1+4+9...+N
//Por ejemplo 5 primeros numeros: 1+4+9+16+25=55

// El valor de N se define directamente aquí
let N = 5; // Puedes cambiar este número para probar

let sumatoria = 0;
let contador = 1;

while (contador <= N) {
    sumatoria = sumatoria + (contador * contador);
    contador = contador + 1;
}

// Mostrar resultados
console.log("La sumatoria de los " + N + " primeros numeros es: " + sumatoria);