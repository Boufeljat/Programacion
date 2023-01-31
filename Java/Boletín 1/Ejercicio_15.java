package com.edu;

import java.util.Scanner;

// Crea un programa que permita sumar N números. El usuario decide cuándo termina
// de introducir números al indicar la palabra ‘fin’

public class Ejercicio_15 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int sum = 0;
		String num;
		System.out.println("Introduce números (escribir 'fin' para salir):");
		do {
			num = scan.next();
			if (!num.equals("fin")) {
				sum += Integer.parseInt(num);
				}
			} while (!num.equals("fin"));
		System.out.println("La suma de los números es " + sum + ".");
		}
}
