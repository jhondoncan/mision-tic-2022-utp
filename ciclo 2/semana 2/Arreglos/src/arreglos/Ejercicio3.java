package arreglos;

import javax.swing.*;


public class Ejercicio3 {
    public static void main(String[] args) {
        // Crea un array de 10 posiciones de números con valores pedidos por teclado. Muestra por consola el índice y el valor al que corresponde
       /* Otra forma
        final int tamanio = 10;
        int[] numeros = new int[tamanio];
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Introduce un número: ");
            Scanner sc = new Scanner(System.in);
            numeros[i] = sc.nextInt();
        }
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("El número " + numeros[i] + " está en la posición " + i);
        }
        */
        final int tamanio = 10;
        int[] num = new int[tamanio];

        // INVOCAR METODOS
        rellenarArray(num);
        mostrarArray(num);

    }

    public static void rellenarArray(int[] lista) {
        for (int i = 0; i < lista.length; i++) {
            int c = i+1;
            String texto = JOptionPane.showInputDialog("Digite un numero: " + c);
            lista[i] = Integer.parseInt(texto);
        }
    }

    public static void mostrarArray(int[] lista) {
        for (int i = 0; i < lista.length; i++) {
            System.out.println("En el indice " + i + " esta almacenado el numero: " + lista[i]);
        }
    }
}
