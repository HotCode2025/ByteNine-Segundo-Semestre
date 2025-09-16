// let persona3 = new Persona('Carla', 'Ponce'); esto no se debe hacer: Persona is not defined

// 6.1 Sintaxis de Clases en JavaScript: Parte 1 y 2 
class Persona{
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }
// 6.2 Método Get y Set: Parte Get y Parte Set
    get nombre(){
        return this._nombre;        
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }

}

class Empleado extends Persona{ // Clase hija
    constructor (nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }
    get departamento(){
        this._departamento;
    }
    set departamento(departamento){
        this._departamento = departamento;
    }

}

let persona1 = new Persona('Martín', 'Perez');
console.log(persona1.nombre);

persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre);

persona1.apellido = 'Martinez';
console.log(persona1.apellido);

// console.log(persona1);
let persona2 = new Persona('Carlos', 'Lara')
console.log(persona2._nombre);

persona2.nombre = 'Maria Laura';
console.log(persona2.nombre);

persona2.apellido = 'Gutierrez'
console.log(persona2.apellido);
// console.log(persona2);

// 6.3 hoisting y clases: Parte 1 y 2


// 6.4 Herencia: Parte 1 y 2  diagrama.uxf

let empleado1 = new Empleado('Maria', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombre);
