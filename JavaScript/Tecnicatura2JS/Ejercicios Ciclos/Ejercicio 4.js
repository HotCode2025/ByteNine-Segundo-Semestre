//Ejercicio 4 Python -> Javascript
//Dadas las horas trabajadas de 5 personas y la tarifa de pago.
//Calcular el salario y la sumatoria de todos los salarios.

let horas = [40, 35, 45, 50, 30];
let tarifa = 15; // Tarifa de pago por hora
let salarios = [];
let sumaSalarios = 0;

for (let i = 0; i < horas.length; i++) {
    let salario = horas[i] * tarifa;
    console.log(`Salario de la persona ${i + 1}: $${salario}`);
    salarios.push(salario);
    sumaSalarios += salario;
}

console.log(`La sumatoria de todos los salarios es: $${sumaSalarios}`);