//Clase 5; Tema Clases y Objetos Parte 3 Tarea
//Punto: 5.8 Ejercicio Ciclos 09 con Scanner y JOptionPane
//Ejercicio 9: Pedir el dia, mes y año de una fecha e indicar 
//si la fecha es correcta. suponiendo que todos los meses
//son de 30 dias
//Clase JOptionPane

function fechaCorrecta() {
  let dia = 15;
  let mes = 8;
  let año = 2025;

  if (mes < 1 || mes > 12) {
    console.log("La fecha no es correcta, ingresaste mal el mes");
    return;
  }

  if (dia < 1 || dia > 30) {
    console.log("La fecha no es correcta: día mal ingresado para este mes.");
    return;
  }

  if (año < 1) {
    console.log("La fecha no es correcta: año equivocado.");
    return;
  }

  console.log("La fecha es correcta: " + dia + "/" + mes + "/" + año);
}

fechaCorrecta();