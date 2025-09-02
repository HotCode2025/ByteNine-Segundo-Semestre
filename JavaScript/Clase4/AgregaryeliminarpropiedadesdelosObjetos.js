let persona = {
    nombre: "Juan",
    apellido: "Perez",
    email: "jgil@gmail.com",
    edad: 28,
    nombreCompleto: function() {
        return this.nombre + ' ' + this.apellido;
        }
    }

persona.apellida = "Lara"; //modificar
delete persona.apellida; //eliminar
console.log(persona);
