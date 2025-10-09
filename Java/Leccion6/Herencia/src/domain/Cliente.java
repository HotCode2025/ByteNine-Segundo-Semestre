/*
 9.5 Herencia parte 5: Presentamos la tarea de hoy
Crear la clase Cliente
 */
package domain;

import java.util.Date;


public class Cliente extends Persona {
    //Creamos los atributos ( Modificador de acceso private
    private int idCliente;
    private Date fechaRegistro;//Importacion de la clase date
    private boolean vip;//Significa Very importsnt person
    private static int contadorCliente; // el contador cliente lo hacemos tipo estatico
    
    //Creamos el constructor completo de la clase padre
    public Cliente(Date fechaRegistro, boolean vip, String nombre,
            char genero, int edad, String direccion){
        super(nombre, genero, edad, direccion);
        
        //Inicilizamos los atributos propios de cliente
        this.idCliente = ++Cliente.contadorCliente; //aumenta de uno en un idcliente
        this.fechaRegistro = fechaRegistro;
        this.vip = vip;
        
    }
    //Añadimos los metodos getter and setter

    public int getIdCliente() {
        return this.idCliente;
    }

    public Date getFechaRegistro() {
        return this.fechaRegistro;
    }

    public void setFechaRegistro(Date fechaRegistro) {
        this.fechaRegistro = fechaRegistro;
    }

    public boolean isVip() {
        return vip;
    }

    public void setVip(boolean vip) {
        this.vip = vip;
    }
    
    //Agregamos metodo to string

   @Override
    public String toString() {
        // Reutilizamos el método toString de la clase Persona con super.toString()
        StringBuilder sb = new StringBuilder();
        sb.append("Cliente{");
        sb.append("idCliente=").append(this.idCliente);
        sb.append(", fechaRegistro=").append(this.fechaRegistro);
        sb.append(", vip=").append(this.vip);
        sb.append(", ").append(super.toString()); // Agregamos la info de Persona
        sb.append('}');
        return sb.toString();
    }
    
    
}
