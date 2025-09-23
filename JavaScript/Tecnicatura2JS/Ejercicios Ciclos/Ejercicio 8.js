// Diseñar un programa que al ingresar un año indique si es bisiesto o no.
//repetir hasta que el usuario lo decida cancelar
// Hacerlo con do while

let respuesta;

do {
    let anio = parseInt(prompt('Ingrese un año y le dire si es bisiesto o no'));

    if ((anio % 4 == 0 && anio % 100 != 0) || (anio % 400 == 0)) {
        console.log(`El año ${anio} es bisiesto`);
    } else {
        console.log(`El año ${anio} no es bisiesto`);
    }
    respuesta = prompt('Desea continuar? (si/no)');
} while (respuesta.toLowerCase() == 'si');

console.log('Gracias por participar!');