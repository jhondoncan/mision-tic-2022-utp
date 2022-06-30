package sentencias;

import javax.swing.*;

public class Ejercicio3 {
    public static void main(String[] args) {
        //Programa que ingresa 4 notas y muestra la nota promedio e indica si el alumno aprobó o no.
        double nota1, nota2, nota3, nota4, promedio;
        nota1 = Float.parseFloat(JOptionPane.showInputDialog("Ingrese la nota 1: "));
        nota2 = Float.parseFloat(JOptionPane.showInputDialog("Ingrese la nota 2: "));
        nota3 = Float.parseFloat(JOptionPane.showInputDialog("Ingrese la nota 3: "));
        nota4 = Float.parseFloat(JOptionPane.showInputDialog("Ingrese la nota 4: "));
        promedio = (nota1 + nota2 + nota3 + nota4) / 4;
        promedio = Math.round(promedio * 100.0) / 100.0;
        if (promedio >= 3 && promedio <= 5) {
            JOptionPane.showMessageDialog(null, "El alumno aprobó con un promedio de: " + promedio);
        } else if (promedio >= 0 && promedio < 3) {
            JOptionPane.showMessageDialog(null, "El alumno reprobó con un promedio de: " + promedio);
        } else{
            JOptionPane.showMessageDialog(null, "Error en el programa, promedio fuera de rango");
        }
   }
}
