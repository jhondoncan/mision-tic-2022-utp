package colegio;

public class Docente extends Persona {
    private int codigoDocente;
    private float sueldo;

    public Docente(String nombre, String apellido, int edad, int codigoDocente, float sueldo) {
        super(nombre, apellido, edad);
        this.codigoDocente = codigoDocente;
        this.sueldo = sueldo;
    }

    public void mostrarDatos() {
        System.out.println("Codigo docente: " + codigoDocente);
        System.out.println("Nombre: " + getNombre());
        System.out.println("Apellido: " + getApellido());
        System.out.println("Edad: " + getEdad());
        System.out.println("Sueldo: " + sueldo);
        System.out.println("---------------");
    }
}
