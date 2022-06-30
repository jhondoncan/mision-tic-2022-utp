package consola;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        System.out.println("Hola mundo");
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingrese su nombre: ");
        String nombre = sc.nextLine(); //Se utiliza Line para strings
        System.out.println("Hola " + nombre + ", bienvenido.");
        System.out.println("Ingrese su edad: ");
        int edad = sc.nextInt(); //Se utiliza Int para enteros
        System.out.println("Ingrese su estatura en metros: ");
        double estatura = sc.nextDouble(); //Se utiliza Double para decimales
        System.out.println("Indique su genero (M o F): ");
        char genero = sc.next().charAt(0); //Se utiliza Char para 1 carácter


        // Imprimir información obtenida
        System.out.println("--- INFORMACIÓN ALMACENADA ---");
        System.out.println("Nombre: " + nombre);
        System.out.println("Edad: " + edad);
        System.out.println("Estatura: " + estatura);
        System.out.println("Genero: " + genero);

    }
}

