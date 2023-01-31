package com.edu;

import java.util.Scanner;

// Pedir 10 valores numéricos que representan el salario mensual de 10 empleados.
// Mostrar su suma y cuantos hay mayores de 1000€

public class Ejercicio_16 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int salario, sum = 0, count = 0;
		System.out.println("Introduce los salarios de 10 empleados:");
		for (int i = 0; i < 10; i++) {
			salario = scan.nextInt();
			sum += salario;
			if (salario > 1000) {
				count++;
				}
			}
		System.out.println("La suma de los salarios es " + sum + ".");
		System.out.println("Hay " + count + " salarios mayores a 1000.");
		}
	}
