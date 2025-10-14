/*10.2 Creamos la Clase Producto*/

class Producto {

    static contadorProducto = 0;

    constructor (nombre, precio){
        this._nombre = nombre;
        this._precio = precio;

        this.idProducto = ++Producto.contadorProducto;
    }

    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }

    get precio(){
        return this._precio;
    }
    set precio(precio){
        this._precio = precio;
    }

    productoCompleto(){
        return `${this.idProducto} ${this._nombre} $${this._precio}`;
    }

    toString(){
        return this.productoCompleto();
    }
}

/*10.4 Creamos la Clase Orden*/

class Orden {

    static contadorProductosAgregados = 0;
    static contadorOrdenes = 0;

    static get MAX_PRODUCTOS(){
        return 5;
    }

    constructor (){
        this.idOrden = ++Orden.contadorOrdenes;
        this.productos = [];
    }

    agregarProducto(producto){
        if(this.productos.length < Orden.MAX_PRODUCTOS){
            this.productos.push(producto);
        } else {
            console.log('No se pueden agregar mas productos a la orden.');
        }
    }

    calcularTotal(){
        let total = 0;
        for (let producto of this.productos){
            total += producto.precio;
        }
        return total;
    }

    mostrarOrden(){
        let ordenInfo = "Orden: ";
        for (let producto of this.productos){
            ordenInfo +=producto.toString() + ";  ";
        }
        ordenInfo += `Total: $${this.calcularTotal()}`;
        return ordenInfo;
    }

}

/*10.3 Prueba de la Clase Producto*/

let producto1 = new Producto("Harina", 800);

console.log(producto1);

producto1.nombre = "Huevo";
producto1.precio = 2500;

console.log(producto1)

let producto2 = new Producto("Harina",800);
let producto3 = new Producto("Levadura",800);
let producto4 = new Producto("Sal",1700);
let producto5 = new Producto("Grasa",3000);
//let producto6 = new Producto("Leche",1700);


// Prueba de la Clase Orden

let orden1 = new Orden();

orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.agregarProducto(producto3);
orden1.agregarProducto(producto4);
orden1.agregarProducto(producto5);
//orden1.agregarProducto(producto6);

console.log(orden1.mostrarOrden());

console.log(producto3);