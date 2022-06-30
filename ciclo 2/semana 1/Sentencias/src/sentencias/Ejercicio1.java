package sentencias;

import javax.swing.*;

public class Ejercicio1 {
    public static void main(String[] args) {
        // Programa que recibe el mes e indica que estación del año es

        //var es una variable universal que permite almacenar strings, int, doubles, etc.
        var mes = Integer.parseInt(JOptionPane.showInputDialog("Ingrese el numero del mes: "));
       /*

       CON SWITCH

       switch (mes) {
            case "12":
            case "1":
            case "2":
                JOptionPane.showMessageDialog(null, "El mes " + mes + " esta en Invierno");
                break;
            case "3":
            case "4":
            case "5":
                JOptionPane.showMessageDialog(null, "El mes " + mes + " esta en Primavera");
                break;
            case "6":
            case "7":
            case "8":
                JOptionPane.showMessageDialog(null, "El mes " + mes + " esta en Verano");
                break;
            case "9":
            case "10":
            case "11":
                JOptionPane.showMessageDialog(null, "El mes " + mes + " esta en Otoño");
                break;
            default:
                JOptionPane.showMessageDialog(null, "El mes " + mes + " no es un mes valido");
                break;
        } */
        var nombreMes = "";
        String estacion = "Estacion desconocida";
        if (mes == 12 || mes == 1 || mes == 2) {
            if (mes == 12) {
                nombreMes = "Diciembre";
            } else if (mes == 1) {
                nombreMes = "Enero";
            } else {
                nombreMes = "Febrero";
            }
            estacion = "Invierno";
        } else if (mes == 3 || mes == 4 || mes == 5) {
            if (mes == 3) {
                nombreMes = "Marzo";
            } else if (mes == 4) {
                nombreMes = "Abril";
            } else {
                nombreMes = "Mayo";
            }
            estacion = "Primavera";
        } else if (mes == 6 || mes == 7 || mes == 8) {
            if (mes == 6) {
                nombreMes = "Junio";
            } else if (mes == 7) {
                nombreMes = "Julio";
            } else {
                nombreMes = "Agosto";
            }
            estacion = "Verano";
        } else if (mes == 9 || mes == 10 || mes == 11) {
            if (mes == 9) {
                nombreMes = "Septiembre";
            } else if (mes == 10) {
                nombreMes = "Octubre";
            } else {
                nombreMes = "Noviembre";
            }
            estacion = "Otoño";
        }
        if (mes >= 1 && mes <= 12) {
            JOptionPane.showMessageDialog(null, "En " + nombreMes + " la estación es " + estacion);
        } else {
            JOptionPane.showMessageDialog(null, "Lo sentimos, " + mes + " no es un mes valido");
        }

    }
}
