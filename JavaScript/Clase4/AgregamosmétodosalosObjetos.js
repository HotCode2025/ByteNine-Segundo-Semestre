let x = 10;
console.log(x.length);
console.log("Tipo: primitivo ");
let persona = {
    nombre: "Juan",
    apellido: "Perez",
    email: "jgil@gmail.com",
    edad: 28,
    nombreCompleto: function() {
        return this.nombre + ' ' + this.apellido;
        }
    }

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.edad);
console.log(persona.email);
console.log(persona.nombreCompleto());
console.log("ejecutando con un objeto: ");
