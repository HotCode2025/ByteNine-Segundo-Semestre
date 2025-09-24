// Ejercicio 13: Factorial con while y do while

let n = 5; // Número fijo para calcular factorial

// usando while
let i = 1;
let factorialWhile = 1;

while (i <= n) {
  factorialWhile *= i;
  i++;
}

// usando do while
let j = 1;
let factorialDoWhile = 1;

if (n === 0) {
  factorialDoWhile = 1; // 0! = 1
} else {
  do {
    factorialDoWhile *= j;
    j++;
  } while (j <= n);
}

console.log("Número:", n);
console.log("Factorial con while:", factorialWhile);
console.log("Factorial con do while:", factorialDoWhile);