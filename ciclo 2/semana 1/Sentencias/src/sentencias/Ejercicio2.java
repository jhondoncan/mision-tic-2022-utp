package sentencias;

import javax.swing.*;

public class Ejercicio2 {
    public static void main(String[] args) {
        // Programa que recibe el mes e indica que estación del año es

        //var es una variable universal que permite almacenar strings, int, doubles, etc.
        var mes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el numero del mes: "));
        String nombreMes = "Mes desconocido";
        String estacion = "Estación desconocida";
        switch (mes) {
            case 12:
            case 1:
            case 2:
                estacion = "Invierno";
                if (mes == 12) {
                    nombreMes = "Diciembre";
                } else if (mes == 1) {
                    nombreMes = "Enero";
                } else {
                    nombreMes = "Febrero";
                }
                break;
            case 3:
            case 4:
            case 5:
                estacion = "Primavera";
                if (mes == 3) {
                    nombreMes = "Marzo";
                } else if (mes == 4) {
                    nombreMes = "Abril";
                } else {
                    nombreMes = "Mayo";
                }
                break;
            case 6:
            case 7:
            case 8:
                estacion = "Verano";
                if (mes == 6) {
                    nombreMes = "Junio";
                } else if (mes == 7) {
                    nombreMes = "Julio";
                } else {
                    nombreMes = "Agosto";
                }
                break;
            case 9:
            case 10:
            case 11:
                estacion = "Otoño";
                if (mes == 9) {
                    nombreMes = "Septiembre";
                } else if (mes == 10) {
                    nombreMes = "Octubre";
                } else {
                    nombreMes = "Noviembre";
                }
                break;
        }
        if (mes >= 1 && mes <= 12) {
            JOptionPane.showMessageDialog(null, "En " + nombreMes + " la estación es " + estacion);
        } else {
            JOptionPane.showMessageDialog(null, "Lo sentimos, " + mes + " no es un mes valido");
        }
    }
}
