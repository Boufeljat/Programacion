package Objeto_2;

import java.util.Scanner;

public class Cuenta {
    private double saldo;
    private int numReintegros;
    private int numIngresos;

    public Cuenta(double saldoInicial) {
        this.saldo = saldoInicial;
        this.numReintegros = 0;
        this.numIngresos = 0;
    }

    public void hacerReintegro(double cantidad) {
        if (cantidad > 0 && cantidad <= saldo) {
            saldo -= cantidad;
            numReintegros++;
            System.out.println("Reintegro de " + cantidad + " euros realizado correctamente.");
        } else {
            System.out.println("Error: cantidad inválida.");
        }
    }

    public void hacerIngreso(double cantidad) {
        if (cantidad > 0) {
            saldo += cantidad;
            numIngresos++;
            System.out.println("Ingreso de " + cantidad + " euros realizado correctamente.");
        } else {
            System.out.println("Error: cantidad inválida.");
        }
    }

    public void consultarSaldo() {
        System.out.println("El saldo actual de la cuenta es: " + saldo + " euros.");
        System.out.println("Número de reintegros realizados: " + numReintegros);
        System.out.println("Número de ingresos realizados: " + numIngresos);
    }

    public double getSaldo() {
        return saldo;
    }
}
