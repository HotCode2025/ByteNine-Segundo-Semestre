let sumar = function(a= 4, b= 5) {
    console.log(arguments.length[0]);
    console.log(arguments.length[1]);
    return a + b;
}
resultado = sumar(1, 2);
console.log(resultado);
