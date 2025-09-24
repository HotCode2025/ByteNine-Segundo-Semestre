//Ejercicio 12: Calcular sumatoria
//Hacer un progrma donde el usuario ingrese un numero N,
//luego le vamos a pedir otro nuero para calcular la potencia
//de los N numeros recorridos, los cuales dividiremos con la
//multiplicacion del factorial y al mismo tiempo sumamos
//en cada recorrido, imprimir el resultado de la suma.

let numero = 5;
let numerox = 2;
let suma = 1;
let i = 1;
let m
let n

while (i <= numero) {
  let factorial = 1;
  let m = 1;
  while (m <= i) {
    factorial *= m;
    m += 1;
  }

  let potencia = 1;
  let n = 0;
  while (n < i) {
    potencia *= numerox;
    n += 1;
  }

  suma += potencia / factorial;
  i += 1;
}

console.log(suma);