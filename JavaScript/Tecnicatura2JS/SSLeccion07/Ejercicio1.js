// Ejercicio 1: Función que valide una contraseña (mínimo 8 caracteres, 1 número, 1 mayúscula)

function validatePassword(password) {

    // Tu código aquí
    const mincaracter = 8;
    
    const tieneMayus = /[A-Z]/.test(password);

    const tieneNum = /[0-9]/.test(password);

    if (tieneMayus && tieneNum && mincaracter <= password.length){
        return true;
    }else{
        return false;
    }
}

console.log(validatePassword("Abc12345")); // true

console.log(validatePassword("weak")); // false