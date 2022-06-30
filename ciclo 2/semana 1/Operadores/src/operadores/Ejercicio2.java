package operadores;

import javax.swing.*;

public class Ejercicio2 {
    public static void main(String[] args) {
        //Programa que promedia 3 notas de un estudiante
        float nota1 = Float.parseFloat(JOptionPane.showInputDialog("Ingrese la nota 1: "));
        float nota2 = Float.parseFloat(JOptionPane.showInputDialog("Ingrese la nota 2: "));
        float nota3 = Float.parseFloat(JOptionPane.showInputDialog("Ingrese la nota 3: "));
        float promedio = (nota1 + nota2 + nota3) / 3;
        JOptionPane.showMessageDialog(null, "El promedio de la materia es: " + (String.format("%.1f",promedio)));

    }

}
