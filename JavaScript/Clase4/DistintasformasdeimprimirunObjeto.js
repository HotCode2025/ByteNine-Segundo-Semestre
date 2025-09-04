let persona = {
    nombre: "Juan",
    apellido: "Perez",
    email: "jgil@gmail.com",
    edad: 28,
    nombreCompleto: function() {
        return this.nombre + ' ' + this.apellido;
        }
    }
//distintas formas de mostrar un objeto
console.log("distintas formas de mostrar un objeto: 1");
//1. concatenar cada valor de cada propiedad
console.log(persona.nombre + ', ' + persona.apellido);
console.log("distintas formas de mostrar un objeto: 2");

//2. for in
for(nombrepropiedad in persona) {
    console.log(persona[nombrepropiedad]);
}
console.log("distintas formas de mostrar un objeto: 3");

//3. Object.values()
let personaArray = Object.values(persona);
console.log(personaArray);

console.log("distintas formas de mostrar un objeto: 3");
//4. JSON.stringify
let personaString = JSON.stringify(persona);
console.log(personaString);