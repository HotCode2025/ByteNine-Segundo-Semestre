
package ar.com.codesystem.ventas;


public class Producto {
    
    //Atributos de la clase
    private int idProducto;
    private String nombre;
    private double precio;
    private static int contadorProductos;
    
    
    //Constructor vacio
    private Producto(){
        this.idProducto = ++Producto.contadorProductos;
        
    }
     
    //Constructor 
    public Producto(String nombre, double precio){
        this();//Llamaos al constructor vacio para el aumento de idProducto
        this.nombre = nombre;
        this.precio = precio;
        
    }

    //Getter and Setter
    public int getIdProducto() {
        return idProducto;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }
    
//Sobreescritura que heredamos de la clase padre object
    @Override
    public String toString() {
        return "Producto{" + "idProducto=" + idProducto + ", nombre=" + nombre + ", precio=" + precio + '}';
    }
    
}
