//Funciones de  tipo self y invoking

let x = function (a, b){ return a + b};

resultado = x(5, 6);

(function(a, b){
    console.log("Ejecucion la funcion: " + (a + b));
})(9, 6);