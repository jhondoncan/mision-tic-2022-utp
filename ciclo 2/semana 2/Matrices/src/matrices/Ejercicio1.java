package matrices;

public class Ejercicio1 {
    public static void main(String[] args) {
        int[][] matriz = new int[3][3];
        int suma = 0;
        for (int i = 0; i < matriz.length; i++) {
            for (int j = 0; j < matriz[i].length; j++) {
                matriz[i][j] = (int) (Math.random() * 10);
                System.out.print(matriz[i][j] + " ");
                suma += matriz[i][j];
            }
            System.out.println();
        }
        System.out.println("La suma de todos los elementos es: " + suma);
    }
}
