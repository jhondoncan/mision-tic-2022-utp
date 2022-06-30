package operadores;

import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        // Programa que calcula el area de un triangulo
        System.out.println("Ingrese el valor de la base del triangulo: ");
        Scanner sc = new Scanner(System.in);
        double base = Double.parseDouble(sc.nextLine());
        System.out.println("Ingrese el valor de la altura del triangulo: ");
        double altura = Double.parseDouble(sc.nextLine());
        double area = (base * altura) / 2;
        System.out.println("El area del triangulo es: " + area);
    }

}
