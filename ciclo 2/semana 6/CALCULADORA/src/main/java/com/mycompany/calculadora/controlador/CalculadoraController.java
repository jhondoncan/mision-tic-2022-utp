package com.mycompany.calculadora.controlador;

import com.mycompany.calculadora.modelo.CalculadoraModelo;
import com.mycompany.calculadora.vista.CalculadoraVista;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CalculadoraController implements ActionListener {

    private final CalculadoraVista view;
    private final CalculadoraModelo model;
    private Operacion operation;

    public CalculadoraController(CalculadoraVista view, CalculadoraModelo model) {
        this.view = view;
        this.model = model;
        this.operation = Operacion.SUMA;
    }

    public void setOperacion(Operacion operation) {
        this.operation = operation;
    }

    public void actionPerformed(ActionEvent e) {

        try {
            model.setNumeroUno(Integer.valueOf(view.getNumeroUno()));
            model.setNumeroDos(Integer.valueOf(view.getNumeroDos()));

            switch (operation) {
                case SUMA:
                    model.sumar();
                    break;
                case RESTA:
                    model.restar();
                    break;
                case MULTIPLICACION:
                    model.multiplicar();
                    break;
                case DIVISION:
                    model.dividir();
                    break;
                case MODULO:
                    model.calcularModulo();
                    break;
                default:
                    throw new UnsupportedOperationException("Operacion no implementada " + operation);
            }
            view.setResultado(model.getResultado().toString());
        } catch (Exception ex) {
            view.mostrarException(ex);
        }
    }
    
    
    public void iniciar(){
    view.iniciar(this);
    }

}
