//Ejercicio 3 Python -> Javascript
//Supongamos que tiene un conjunto de calificaciones de un grupo de 10 estudiantes.
//1-Realizar un algoritmo para calcular la clificacion promedio y la calificacion mas baja
//de todo el grupo.

let calificaciones = [8, 7, 9, 6, 5, 10, 4, 3, 2, 1];
let sumaCalif = 0;
let calificacionBaja = calificaciones[0];

for (let i = 0; i < calificaciones.length; i++) {
    
    if (calificaciones[i] < calificacionBaja) {
        calificacionBaja = calificaciones[i];
    }
}

for (let a = 0; a < calificaciones.length; a++) {
    sumaCalif += calificaciones[a];
    promedioCalif = sumaCalif / 10;
}

console.log("El promedio de las calificaciones es: " + promedioCalif);
console.log("La calificacion mas baja es: " + calificacionBaja);