package Objeto_1;

import java.util.Scanner;

import javax.swing.JOptionPane;

public class Rectangulo {
    private double longitud;
    private double ancho;
    private static final double VALOR_PREDETERMINADO = 1.0;

    public Rectangulo() {
        this.longitud = VALOR_PREDETERMINADO;
        this.ancho = VALOR_PREDETERMINADO;
    }

    public Rectangulo(double longitud, double ancho) {
        setLongitud(longitud);
        setAncho(ancho);
    }

    public double getLongitud() {
        return longitud;
    }

    public double getAncho() {
        return ancho;
    }

    public void setLongitud(double longitud) {
        if (longitud > 0 && longitud < 20) {
            this.longitud = longitud;
        }
    }

    public void setAncho(double ancho) {
        if (ancho > 0 && ancho < 20) {
            this.ancho = ancho;
        }
    }

    public double calcularPerimetro() {
        return 2 * (longitud + ancho);
    }

    public double calcularArea() {
        return longitud * ancho;
    }
}



