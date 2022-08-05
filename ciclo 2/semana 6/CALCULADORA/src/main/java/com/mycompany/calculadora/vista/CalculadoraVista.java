
package com.mycompany.calculadora.vista;

import com.mycompany.calculadora.controlador.CalculadoraController;


public interface CalculadoraVista {
    public String getNumeroUno();
    public String getNumeroDos();
    public void setResultado(String resultado);
    public void iniciar(CalculadoraController controller);
    public void mostrarException(Exception ex);
}
