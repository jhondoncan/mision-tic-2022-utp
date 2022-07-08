package arreglos;

import javax.swing.*;

public class Ejercicio4 {
    public static void main(String[] args) {
        String texto = JOptionPane.showInputDialog("Digite el tamaño del arreglo: ");
        int[] num = new int[Integer.parseInt(texto)];

        //INVOCAR METODOS
        llenarArregloAleatorio(num, 0, 9);
        mostrarArray(num);
    }

    public static void llenarArregloAleatorio(int[] lista, int a, int b) {
        for (int i = 0; i < lista.length; i++) {
            // Generar un numero aleatio entre 0 y 9
            lista[i] = (int) (Math.random() * (a - b) + b);
        }
    }

    public static void mostrarArray(int[] lista) {
        for (int i = 0; i < lista.length; i++) {
            System.out.println("En el indice " + i + " esta almacenado el numero: " + lista[i]);
        }
    }

}
