// Maxi
// Ingresar N numeros
// Calcular el maximo y minimo de ellos.

let numeros = [15, 8, 2, 60, 10, 3, 50];
let contador = 1;
let mayor = numeros[0];
let menor = numeros[0];
let numero

while (contador < numeros.length){
    let numero = numeros[contador];
    
    if (numero > mayor){
        mayor = numero;
    
    }
    if (numero < menor){
        menor = numero;
    }
    contador++;
}
console.log("El mayor de los numeros ingresados es: " + mayor);
console.log("El menor de los numeros ingresados es: " + menor);
