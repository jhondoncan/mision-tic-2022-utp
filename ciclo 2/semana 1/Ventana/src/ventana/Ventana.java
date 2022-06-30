package ventana;

import javax.swing.*;

public class Ventana {
    public static void main(String[] args) {
        String cadena;
        int entero;
        char letra;
        double decimal;

        cadena = JOptionPane.showInputDialog("Introduce una cadena");
        entero = Integer.parseInt(JOptionPane.showInputDialog("Introduce un entero"));
        letra = JOptionPane.showInputDialog("Introduce una letra").charAt(0);
        decimal = Double.parseDouble(JOptionPane.showInputDialog("Introduce un numero decimal"));

    }
}
