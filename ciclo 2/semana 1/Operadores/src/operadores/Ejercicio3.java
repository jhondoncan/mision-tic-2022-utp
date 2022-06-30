package operadores;

import javax.swing.*;

public class Ejercicio3 {
    public static void main(String[] args) {
        //Programa que resta 3 gastos de un sueldo
        double sueldo = Double.parseDouble(JOptionPane.showInputDialog("Ingrese el sueldo: "));
        double gasto1 = Double.parseDouble(JOptionPane.showInputDialog("Ingrese el gasto 1: "));
        double gasto2 = Double.parseDouble(JOptionPane.showInputDialog("Ingrese el gasto 2: "));
        double gasto3 = Double.parseDouble(JOptionPane.showInputDialog("Ingrese el gasto 3: "));
        double resta = sueldo - (gasto1 + gasto2 + gasto3);
        JOptionPane.showMessageDialog(null, "El sueldo restante es: " + resta);
    }
}
