package com.edu;

import java.util.Scanner;

// Método que pida 15 números y realice su suma.

public class Ejercicio_8 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int suma = 0;
		for (int i = 1; i <= 15; i++) {
			System.out.print("Introduce el número " + i + ": ");
			int num = sc.nextInt();
			suma += num;
		}
		System.out.println("La suma de los 15 números es: " + suma);
  }
}
