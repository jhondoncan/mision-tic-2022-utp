package arreglos;

public class Ejercicio2 {
    public static void main(String[] args) {
        String tecnologia[]={"Televisores","Computadoras","Tablets","Celulares","Videojuegos"};
        double precio[]={20000.05,15000.30,12000.99,10000.20,8000.00};
        for (int i = 0; i < tecnologia.length; i++) {
            System.out.println(tecnologia[i]+": "+precio[i]);
        }
    }
}

