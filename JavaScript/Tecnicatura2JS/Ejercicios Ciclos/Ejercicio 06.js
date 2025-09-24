// Ejercicio 6: ingresar N numeros
// Mostrar la suma de los pares, cuántos pares hay y el promedio de los impares.

let numeros = [3, 8, 5, 12, 7, 4];
let N = numeros.length;

let i = 0;
let sumaPares = 0;
let cantidadPares = 0;
let sumaImpares = 0;
let cantidadImpares = 0;

while (i < N) {
  let num = numeros[i];
  
  if (num % 2 === 0) {
    sumaPares += num;
    cantidadPares++;
  } else {
    sumaImpares += num;
    cantidadImpares++;
  }
  i++;
}

let promedioImpares = cantidadImpares > 0 ? (sumaImpares / cantidadImpares) : 0;

console.log("Suma de pares:", sumaPares);
console.log("Cantidad de pares:", cantidadPares);
console.log("Promedio de impares:", promedioImpares);