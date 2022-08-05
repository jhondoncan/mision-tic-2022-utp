package com.mycompany.calculadora.vista;

import com.mycompany.calculadora.controlador.CalculadoraController;
import com.mycompany.calculadora.controlador.Operacion;
import java.nio.Buffer;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class CalculadoraConsola implements CalculadoraVista {

    private CalculadoraController controller;
    private String numeroUno;
    private String numeroDos;

    private void menuPrincipal() {
        try ( var input = new BufferedReader(new InputStreamReader(System.in))) {
            var mainLoop = true;
            while (mainLoop) {
                System.out.println("CALCULADORA MANUAL");
                System.out.println("Puedes realizar operaciones aritméticas");
                System.out.println("'+': Suma");
                System.out.println("'-': Resta");
                System.out.println("'*': Multiplicación");
                System.out.println("'/': División");
                System.out.println("'%': Modulo");
                System.out.println("'.': Salir");
                System.out.println("Ingrese el simbolo de la operacion que desea ejecutar");

                var opcion = input.readLine();
                switch (opcion) {
                    case "+":
                        controller.setOperacion(Operacion.SUMA);
                        break;
                    case "-":
                        controller.setOperacion(Operacion.RESTA);
                        break;
                    case "*":
                        controller.setOperacion(Operacion.MULTIPLICACION);
                        break;
                    case "/":
                        controller.setOperacion(Operacion.DIVISION);
                        break;
                    case "%":
                        controller.setOperacion(Operacion.MODULO);
                        break;
                    case ".":
                        System.out.println("Hasta la proxima amiguito");
                        mainLoop = false;
                        continue;
                    default:
                        System.err.println("¡La opcion " + opcion + " no es valida!");
                        System.out.println("Presione 'Enter' para continuar...");
                        input.readLine();
                        continue;
                }
                System.out.println("Ingrese el primer numero: ");
                numeroUno = input.readLine();
                System.out.println("Ingrese el segundo numero: ");
                numeroDos = input.readLine();

                controller.actionPerformed(null);
                System.out.println("Precione 'Enter' para continuar");
                input.readLine();
            }
        } catch (IOException ex) {
            System.err.println("Error en nuestro sistema ¡Lo sentimos!" + ex.getMessage());

        }
    }

    @Override
    public String getNumeroUno() {
        return numeroUno;
    }

    @Override
    public String getNumeroDos() {
        return numeroDos;
    }

    @Override
    public void setResultado(String resultado) {
        System.out.println("El resultado es: " + resultado);
    }

    @Override
    public void iniciar(CalculadoraController controller) {
        this.controller = controller;
        menuPrincipal();
    }

    @Override
    public void mostrarException(Exception ex) {
        System.err.println("Exception: " + ex.getMessage());
    }

}
