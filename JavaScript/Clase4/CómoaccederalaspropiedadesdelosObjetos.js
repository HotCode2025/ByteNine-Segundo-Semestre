let persona = {
    nombre: "Juan",
    apellido: "Perez",
    email: "jgil@gmail.com",
    edad: 28,
    nombreCompleto: function() {
        return this.nombre + ' ' + this.apellido;
        }
    }


//for in
for(propiedad in persona) {
    console.log(propiedad);
    console.log(persona[propiedad]);
}
