package arreglos;

public class Ejercicio1 {
    public static void main(String[] args) {
        String[] productos = {"Leche", "Huevos", "Pan", "Carne", "Pollo", "Lentejas", "Pescado", "Cerezas", "Café", "Agua"};
        double[] precios = {1.50, 2.00, 1.80, 3.00, 2.30, 1.00, 2.00, 1.40, 1.60, 1.55};
        System.out.println("Lista de productos con sus precios");
        for (int i = 0; i < productos.length; i++) {
            System.out.println(productos[i] + ": " + precios[i]);
        }
    }
}
