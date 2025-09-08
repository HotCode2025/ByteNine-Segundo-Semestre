let persona = {
    nombre: "Juan",
    apellido: "Perez",
    email: "jgil@gmail.com",
    edad: 28,
    nombreCompleto: function() {
        return this.nombre + ' ' + this.apellido;
        }
    }