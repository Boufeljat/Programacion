package com.edu;

import java.util.Scanner;

// Realiza un programa que pida números y muestre su cuadrado, repitiendo el
// proceso hasta que se introduzca un número negativo.


import java.util.Scanner;

public class Ejercicio_11 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int num;
		System.out.println("Introduce números para obtener su cuadrado (introduce un número negativo para salir):");
		do {
    	num = scan.nextInt();
    	if (num >= 0) {
    		System.out.println("El cuadrado de " + num + " es " + num * num);
    	}
    	} while (num >= 0);
    		System.out.println("Programa terminado.");
    }
}
