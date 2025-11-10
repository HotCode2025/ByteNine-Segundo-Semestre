//CLASE 4:tema:Clases y Objetos Poo parte 2 Tarea
//Punto: 4.7 Ejercicio con ciclos 7 con la Clase Scanner y JoptionPane
//Ejercicio 7: Pedir numeros hasta que se introduzca uno negativo, 
//y calcular la media

function promedioNumeros() {
  let numeros = [8, 30, 46, -10];
  let suma = 0;
  let conteo = 0;

  for (let i = 0; i < numeros.length; i++) {
    if (numeros[i] < 0) {
      break;
    }
    suma += numeros[i];
    conteo++;
  }

  if (conteo === 0) {
    console.log("No se puede calcular el promedio");
  } else {
    let promedio = suma / conteo;
    console.log("El promedio es: " + promedio);
  }
}

promedioNumeros();