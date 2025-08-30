//sumar todo los argumentos
let respuesta = sumartodo(1, 2, 3, 4, 5);
console.log(respuesta);
function sumartodo() {
    let suma = 0;
    for(let i = 0; i < arguments.length; i++) {
        suma += arguments[i];
    }
    return suma;
}
