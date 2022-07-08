package matrices;

import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite el valir de las filas: ");
        int filas = sc.nextInt();
        System.out.println("Digite el valir de las columnas: ");
        int columnas = sc.nextInt();
        int[][] matriz = new int[filas][columnas];
        for (int i =0;i < matriz.length; i++){
            for (int j = 0; j < matriz[i].length; j++) {
                matriz[i][j] = generarNumeroAleatorio(0, 10);
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }

    }
    public static  int generarNumeroAleatorio(int min, int max) {
        return (int) (Math.random() * (max - min + 1)) + min;
    }
}
