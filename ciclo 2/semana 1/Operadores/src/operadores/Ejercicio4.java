package operadores;

import javax.swing.*;

public class Ejercicio4 {
    public static void main(String[] args) {
        //Programa que resuelve operaciones matematicas
        float x = Float.parseFloat(JOptionPane.showInputDialog("Ingrese el valor de x: "));
        float resultado = ((7 * (3 * x + 2)) - 5 * ((4 * x - 3) - 1)) / 4;
        JOptionPane.showMessageDialog(null, "El resultado de la formula es: " + resultado);

    }
}
