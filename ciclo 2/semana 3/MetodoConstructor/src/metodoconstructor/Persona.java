package metodoconstructor;

public class Persona {

        // Atributos
        int id;
        String apellidos;
        String nombre;
        String genero;
        int edad;

        // Metodos
        // public void son los que no generan ningun retorno

        // Metodos constructores


    public Persona(int id, String apellidos, String nombre, String genero, int edad) {
        this.id = id;
        this.apellidos = apellidos;
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
    }

    public void mostrarResultados(){
        System.out.println("Id: " + id);
        System.out.println("Apellidos: " + apellidos);
        System.out.println("Nombre: " + nombre);
        System.out.println("Genero: " + genero);
        System.out.println("Edad: " + edad);
    }

}
