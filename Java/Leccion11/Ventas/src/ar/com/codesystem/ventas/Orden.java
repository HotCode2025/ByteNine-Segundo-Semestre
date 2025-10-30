
package ar.com.codesystem.ventas;

public class Orden {
    private int idOrden;
    private Producto productos[]; //Declaramos el arreglo
    private static int contadorOrdenes;
    private int contadorProductos;
    private static final int MAX_PRODUCTOS = 10;
    
    //Constructor vacio
    public Orden(){
        this.idOrden = ++Orden.contadorOrdenes;
        this.productos = new Producto[Orden.MAX_PRODUCTOS];
    }
    
    // 13.4 Comenzamos con la clase Orden: Parte 2
    public void agregarProducto(Producto producto){
        if(this.contadorProductos < Orden.MAX_PRODUCTOS){
            this.productos[this.contadorProductos++] = producto;
        }else{
            System.out.println("Se ah superado el maximo de productos: "+Orden.MAX_PRODUCTOS);
        }
    }
}
