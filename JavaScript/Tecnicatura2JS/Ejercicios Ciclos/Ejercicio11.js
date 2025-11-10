//Ejercicio 11 Python -> JavaScript
//Leer 10 numeros e imprimir cuantos son positivos, negativos y neutro

let listanum = [0,0,0,0,0,0,5,6,-8,-10];

let contadorP = 0;
let contadorN = 0;
let contadorNe = 0;

for (let i = 0; i <= 10; i++){

    numero = listanum[i];

    if (numero > 0){
        contadorP += 1; 
    }if (numero < 0){
        contadorN += 1;
    }if(numero == 0){
        contadorNe += 1;
    }
}

console.log("La cantidad de numeros positivos es " + contadorP);
console.log("La cantidad de numeros negativos es " + contadorN);
console.log("La cantidad de numeros neutros es " + contadorNe);