package ciclos;

public class Ciclo4 {
    public static void main(String[] args) {
        // Programa que cuenta cuantos numeros del 0 al 10000 son multiplos de 20
           int contador = 0;
              for (int i = 1; i <= 10000; i++) {
                if (i % 20 == 0) {
                     contador++;
                }
              }
        System.out.println("La cantidad de multiplos de 20 entre el 0 y el 10000  son: " + contador);
    }
}
