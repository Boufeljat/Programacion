package com.edu;

import java.util.Scanner;

// Método que pida 5 números e imprima si alguno es múltiplo de 3

public class Ejercicio_9 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		boolean encontrado = false;
		for (int i = 1; i <= 5; i++) {
			System.out.print("Introduce el número " + i + ": ");
			int num = sc.nextInt();
			if (num % 3 == 0) {
				System.out.println("El número " + num + " es múltiplo de 3.");
				encontrado = true;
				break;
			}
		}
		if (!encontrado) {
			System.out.println("No se ha encontrado ningún número múltiplo de 3.");
		}
	}
}
