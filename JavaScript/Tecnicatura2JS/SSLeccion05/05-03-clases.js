class Persona {
    constructor(nombre, apellido) {
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre(){
        return this._nombre;
    }

}

let Persona1 = new Persona("Martin", "Perez");
console.log(Persona1.nombre)
// console.log(persona1);

let Persona2 = new Persona("Carlos", "Lara");
console.log(Persona2.nombre);
//console.log(persona2);