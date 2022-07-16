package colegio;

public class Main {
    public static void main(String[] args) {

        Estudiante estudiante = new Estudiante("Juan", "Perez", 20, 16726, 8.5f);
        Estudiante estudiante2 = new Estudiante("Rocio", "Ramirez", 24, 16765, 7.5f);
        estudiante.mostrarDatos();
        estudiante2.mostrarDatos();

        Docente docente = new Docente("Andres", "Andrade", 30, 98123, 2200000);
        Docente docente2 = new Docente("Maria", "Hernandez", 34, 98231, 2150000);
        docente.mostrarDatos();
        docente2.mostrarDatos();

    }
}
