//Clase 5; Tema Clases y Objetos Parte 3 Tarea
//Punto: 5.8 Ejercicio Ciclos 09 con Scanner y JOptionPane
//Ejercicio 9: Pedir el dia, mes y año de una fecha e indicar 
//si la fecha es correcta. suponiendo que todos los meses
//son de 30 dias
//Clase Scanner

function sumarNumeros() {
  const numeros = [8, 2, 5, 6, 10, 13, 4, 1, 7, 20];
  let suma = 0;

  for (let i = 0; i < numeros.length; i++) {
    suma += numeros[i];
  }

  console.log("La suma total es: " + suma);
}

sumarNumeros();