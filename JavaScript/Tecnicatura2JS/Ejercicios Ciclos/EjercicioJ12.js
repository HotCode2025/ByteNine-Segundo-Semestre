//CLASE 6:B. Programacion Orientada a objetos parte 5-Tarea
//Punto: 7.3 Ejercicio Ciclos 12: Con Clase Scanner y JOption
//Ejercicio 12: Pedir un numero y calcular su factorial
//Hacerlo con la clase JOptionPane

function calcularFactorial() {
  const numero = 30;
  if (numero < 0) {
    console.log("No puede existir factorial para los numeros negativos.");
    return;
  }

  let factorial = 1;
  for (let i = 1; i <= numero; i++) {
    factorial *= i;
  }

  console.log("El factorial de " + numero + " es: " + factorial);
}

calcularFactorial();