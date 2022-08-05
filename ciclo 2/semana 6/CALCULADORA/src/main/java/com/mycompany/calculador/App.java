
package com.mycompany.calculador;
import com.mycompany.calculadora.controlador.CalculadoraController;
import com.mycompany.calculadora.modelo.CalculadoraModelo;
import com.mycompany.calculadora.vista.CalculadoraConsola;
import com.mycompany.calculadora.vista.CalculadoraVista;
        

public class App {
    private enum TipoVista{
    SUMA, RESTA, MULTIPLICACION, DIVISION, MODULO, CONSOLA
    }
    
    public static void main(String[] args) {
        var tipo= TipoVista.CONSOLA;
        CalculadoraVista view = null;
        
        switch (tipo){
            case CONSOLA:
                view = new CalculadoraConsola();
                break;
        }
        var model = new CalculadoraModelo();
        var controller = new CalculadoraController(view, model);
        controller.iniciar();
    }
}
