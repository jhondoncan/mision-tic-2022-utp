package sentencias;

import javax.swing.*;

public class Ejericio4 {
    public static void main(String[] args) {
        // Programa que almacena articulos de una tienda y los muestra en una tabla si son mas de 5 articulos pga en efectivo sino en tarjeta.
        String nombreCliente = JOptionPane.showInputDialog("Ingrese el nombre del cliente: ");
        int articulos = Integer.parseInt(JOptionPane.showInputDialog("Ingrese la cantidad de articulos a facturar: "));
        if (articulos > 0  && articulos <= 5) {
            JOptionPane.showMessageDialog(null, "El cliente " + nombreCliente + " debe pagar en efectivo");
        } else if (articulos > 5 && articulos < 12) {
            JOptionPane.showMessageDialog(null, "El cliente " + nombreCliente + " debe pagar con tarjeta");
        } else if (articulos >= 12) {
            JOptionPane.showMessageDialog(null, "El cliente " + nombreCliente + " debe pagar con cheque");
        } else {
            JOptionPane.showMessageDialog(null, "Error en el programa, cantidad de articulos fuera de rango");
        }

    }
}
