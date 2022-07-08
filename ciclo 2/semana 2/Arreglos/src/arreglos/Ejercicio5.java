package arreglos;

public class Ejercicio5 {
    public static void main(String[] args) {
        //Crear array con numeros de 100 posisiones del 1 al 100 y se suma todos ellos
        int[] num = new int[100];
        int suma = 0;
        double media;
        for (int i = 0; i < num.length; i++) {
            num[i] = i + 1;
            suma += num[i];
        }
        System.out.println("La suma de todos los numeros del 1 al 100 es: " + suma);
        media = (double)suma / num.length;
        System.out.println("La media de todos los numeros del 1 al 100 es: " + media);
    }

}

