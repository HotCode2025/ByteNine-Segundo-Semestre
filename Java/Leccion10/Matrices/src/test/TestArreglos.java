package test;


public class TestArreglos {
    //11.1 Arreglos Parte 1: Creamos la carpeta Leccion9

    public static void main(String[] args) { //Lado derecho instanciamos un objeto de tipo object
        
        int edades[] = new int[3]; //El lado izquiero declaramos la variable
        
        System.out.println("edades = " + edades);
        
        edades[0] = 17;
        System.out.println("edades 0 = " + edades[0]);
        
        edades[1] = 22;
        System.out.println("edades = " + edades[1]);
        
        edades[2] = 18;
        System.out.println("edades = " + edades[2]);
        
        //edades[3] = 7;//Fuera de rango, error en tiempo de ejecucion
        
        for(int i = 0; i < edades.length;i++){
            System.out.println("Edades y sus elementos "+(i+1)+": "+edades[i]);
        }
    }
}
