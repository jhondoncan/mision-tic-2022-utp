public class Computadores {

    public static final Integer PESO_BASE = 5;
    public static final char CONSUMO_W = 'F';
    public static final Double PRECIO_BASE = 100.0;

    public Double precioBase;
    public Integer peso;
    public char consumoW;

    public Computadores() {
        this.precioBase = PRECIO_BASE;
        this.peso = PESO_BASE;
        this.consumoW = CONSUMO_W;
    }

    public Computadores(Double precioBase, Integer peso) {
        this.precioBase = precioBase;
        this.peso = peso;
        this.consumoW = CONSUMO_W;
    }

    public Computadores(Double precioBase, Integer peso, char consumoW) {
        this.precioBase = precioBase;
        this.peso = peso;
        this.consumoW = consumoW;
    }

    public Double calcularPrecio() {
        Double adicion = 0.0;
        // Código

        switch (consumoW) {
            case 'A':
                adicion += 100;
                break;
            case 'B':
                adicion += 80;
                break;
            case 'C':
                adicion += 60;
                break;
            case 'D':
                adicion += 50;
                break;
            case 'E':
                adicion += 30;
                break;
            case 'F':
                adicion += 10;
                break;
        }

        if(peso>=0&peso<19){
            adicion+=10;
        }else if(peso>=20&peso<49){
            adicion+=50;
        }else if(peso>=50&peso<=79){
            adicion+=80;
        }else if(peso>=80){
            adicion+=100;
        }

        return precioBase+adicion;
    }

    public Double getPrecioBase() {
        return precioBase;
    }

    public Integer getPeso() {
        return peso;
    }

    public char getConsumoW() {
        return consumoW;
    }

}

public class ComputadoresMesa extends Computadores{
    private final static Integer ALMACENAMIENTO_BASE = 50;
    private Integer almacenamiento;

    public ComputadoresMesa() {
        this(PRECIO_BASE, PESO_BASE, CONSUMO_W, ALMACENAMIENTO_BASE);
    }

    public ComputadoresMesa(Double precioBase, Integer peso) {
        super(precioBase, peso);
        this.almacenamiento=ALMACENAMIENTO_BASE;
    }

    public ComputadoresMesa(Double precioBase, Integer peso, char consumoW, Integer almacenamiento) {
        super(precioBase, peso, consumoW);
        this.almacenamiento = almacenamiento;
    }

    public Double calcularPrecio() {
        // Código return adicion;
        Double adicion = super.calcularPrecio();

        if (almacenamiento>100){
            adicion+=50;
        }
        return adicion;
    }

    public Integer getCarga() {
        return almacenamiento;
    }

}

public class ComputadoresPortatiles extends Computadores{
    private final static Integer PULGADAS_BASE = 20;
    private Integer pulgadas;
    private boolean camaraITG;

    public ComputadoresPortatiles() {
        this.peso=PESO_BASE;
        this.precioBase=PRECIO_BASE;
        this.consumoW=CONSUMO_W;
        this.pulgadas=PULGADAS_BASE;
        this.camaraITG=false;
    }

    public ComputadoresPortatiles(Double precioBase, Integer peso) {
        super(precioBase, peso);
        this.pulgadas=PULGADAS_BASE;
        this.camaraITG=false;
    }

    public ComputadoresPortatiles(Double precioBase, Integer peso, char consumoW, Integer pulgadas, boolean camaraITG) {
        super(precioBase, peso, consumoW);
        this.pulgadas = pulgadas;
        this.camaraITG = camaraITG;
    }

    // Métodos
    public Double calcularPrecio() {
        // Método Código return adicion;
        Double adicion = super.calcularPrecio();

        if(pulgadas>40){
            adicion+=super.getPrecioBase()*0.3;
        }
        if(camaraITG){
            adicion+=50.0;
        }
        return adicion;
    }


}

public class PrecioTotal {

    private Double totalComputadores = 0.0;
    private Double totalComputadoresPortatiles = 0.0;
    private Double totalComputadoresMesa = 0.0;
    private Computadores[] listaComputadores;

    public PrecioTotal(Computadores[] listaComputadores) {
        this.listaComputadores = listaComputadores;
    }

    public void mostrarTotales() {
// Código

        for (int i = 0; i < listaComputadores.length; i++) {
            if(listaComputadores[i] instanceof Computadores){
                totalComputadores+=listaComputadores[i].calcularPrecio();
            }
            if(listaComputadores[i] instanceof ComputadoresMesa){
                totalComputadoresMesa+=listaComputadores[i].calcularPrecio();
            }
            if(listaComputadores[i] instanceof ComputadoresPortatiles){
                totalComputadoresPortatiles+=listaComputadores[i].calcularPrecio();
            }
        }
// Mostramos los resultados
        System.out.println("La suma del precio de los computadores es de " + totalComputadores);
        System.out.println("La suma del precio de los computadores de mesa es de " + totalComputadoresMesa);
        System.out.print("La suma del precio de los computadores portátiles es de " + totalComputadoresPortatiles);
    }
}