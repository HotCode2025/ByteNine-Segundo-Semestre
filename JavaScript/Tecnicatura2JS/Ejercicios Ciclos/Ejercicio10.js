// Ejercicio 10 PSeint ---> JavaScript :
// Ingresar N números, calcular el máximo y minimos de ellos

let n_elementos;
let i;
let num, mayor, menor;

// Validamos que la cantidad de elementos sea mayor a 0

do{
    n_elementos = parseInt(prompt("Digite un número de elementos: "));

}while (n_elementos <=0);

// Leer el primer número
num = parseFloat(prompt("1.Digite un número: "));
mayor = num;
menor = num;

// Inicializamos el iterador en 2
i = 2;

// Repetimos hasta llegar al número de elementos
do{
    num = parseFloat(prompt(i+". Digite un número: "));

    if (num > mayor){
        mayor = num; // Nuevo N mayor
    } else if (num < menor){
        menor = num; // Nuevo N menor
    }
    i++;
}while (i <= n_elementos);

// Mostramos los resultados
console.log("El mayor de los números ingresados es: " +mayor);
console.log("El menor de los números ingresados es: " +menor);