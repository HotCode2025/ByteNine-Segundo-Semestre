package ar.com.codesystem.ventas.test;

import ar.com.codesystem.ventas.*;

public class VentasTest {

    public static void main(String[] args) {
        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29900.00);
        // Crear mas objetos de tipo Producto = 10
        Producto producto3 = new Producto("Remera", 5200.00);
        Producto producto4 = new Producto("Zapatillas", 15800.00);
        Producto producto5 = new Producto("Bufanda", 3500.00);
        Producto producto6 = new Producto("Gorro", 2800.00);
        Producto producto7 = new Producto("Medias", 1200.00);
        Producto producto8 = new Producto("Cinturon", 4500.00);
        Producto producto9 = new Producto("Guantes", 6200.00);
        Producto producto10 = new Producto("Traje", 45000.00);
        Producto producto11 = new Producto("Corbata", 6000.00);
        Producto producto12 = new Producto("Camisa", 18000.00);
        
        Orden orden1 = new Orden();
        // Agregamos productos al arreglo para Mostrar la Primera Orden
        System.out.println("\n--- ORDEN 1 ---\n");
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();
        
        // Tarea
        // Crear mas objetos de tipo Producto = 10
        // Crear mas objeto de tipo Orden = 2
        
        System.out.println("\n--- ORDEN 2 ---\n");
        
        // Crear y mostrar la segunda orden
        Orden orden2 = new Orden();
        orden2.agregarProducto(producto3);
        orden2.agregarProducto(producto4);
        orden2.agregarProducto(producto5);
        orden2.mostrarOrden();
        
        System.out.println("\n--- ORDEN 3 ---\n");
        
        // Crear y mostrar la tercera orden
        Orden orden3 = new Orden();
        orden3.agregarProducto(producto6);
        orden3.agregarProducto(producto7);
        orden3.agregarProducto(producto8);
        orden3.agregarProducto(producto9);
        orden3.agregarProducto(producto10);
        orden3.mostrarOrden();
        
        
    }
    
}
