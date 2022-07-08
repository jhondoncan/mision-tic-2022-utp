package matrices;

import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        System.out.println("Digite el tamaño de la matriz: ");
        int dimension = entrada.nextInt();

        int[][] matriz1 = new int[dimension][dimension];
        int[][] matriz2 = new int[dimension][dimension];
        int[][] matrizResultado = new int[dimension][dimension];

        for (int i = 0; i < matriz1.length; i++) {
            for (int j = 0; j < matriz1[i].length; j++) {
                System.out.println("Digite el valor de la fila: "+ i + " y de la columna: " + j + " de la matriz 1: ");
                matriz1[i][j] = entrada.nextInt();
                System.out.println("Digite el valor de la fila: "+ i + " y de la columna: " + j + " de la matriz 2: ");
                matriz2[i][j] = entrada.nextInt();
                //System.out.print(matriz1[i][j] + " ");
                matrizResultado[i][j] = matriz1[i][j] + matriz2[i][j];
                //System.out.print(matrizResultado[i][j] + " ");


            }
            System.out.println("Las matriz 1 es: ");
            mostrarMatriz (matriz1);
            System.out.println("Las matriz 2 es: ");
            mostrarMatriz (matriz2);
            System.out.println("Resultado de suma de matrices: ");
            mostrarMatriz (matrizResultado);
        }


    }
    public static  void mostrarMatriz (int[][] matriz) {

        for (int[] ints : matriz) {
            for (int anInt : ints) {
                System.out.print(anInt + " ");
            }
            System.out.println();
        }
    }

}
