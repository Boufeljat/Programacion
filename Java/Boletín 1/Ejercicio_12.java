package com.edu;

import java.util.Scanner;

// Realiza un programa que pida números hasta que se teclee uno negativo y muestre
// cuántos números se han introducido.

public class Ejercicio_12 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int num, count = 0;
		System.out.println("Introduce números (introduce un número negativo para salir):");
		do {
			num = scan.nextInt();
			if (num >= 0) {
				count++;
			}
    		} while (num >= 0);
		System.out.println("Se han introducido " + count + " números.");
	}
}
