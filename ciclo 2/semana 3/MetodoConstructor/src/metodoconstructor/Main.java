package metodoconstructor;

public class Main {
    public static void main(String[] args) {
        Persona persona = new Persona(1, "Perez", "Juan", "M", 30);
        persona.mostrarResultados();
        System.out.println("---------------");
        Persona persona2 = new Persona(2, "Gomez", "Rocio", "F", 25);
        persona2.mostrarResultados();
        System.out.println("---------------");
    }
}
