//Clase 5; Tema Clases y Objetos Parte 3 Tarea Punto: 5.7 Ejercicio Ciclos 08 con Scanner y JOptionPane
//Ejercicio 8: Pedir un numero N, y mostrar todos los numeros del 1 al N.
//Clase JOptionPane

function mostrarNumerosN() {
  const N = 96;
  let numeros = [];

  for (let i = 1; i <= N; i++) {
    numeros.push(i);
  }

  console.log("Los numeros del 1 al " + N + " son:");
  for (let i = 0; i < numeros.length; i++) {
    console.log(numeros[i]);
  }
}

mostrarNumerosN();