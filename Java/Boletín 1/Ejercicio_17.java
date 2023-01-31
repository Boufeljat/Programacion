package com.edu;

import java.util.Scanner;

// Escribe un programa que muestre los N primeros términos de la serie de Fibonacci.
// El primer término de la serie de Fibonacci es 1, el segundo es 1 y el resto se calcula
// sumando los dos anteriores, por lo que tendríamos que los términos son 1, 1, 2, 3, 5,
// 8, 13, 21, 34, 55, 89, 144.

public class Ejercicio_17 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n, a = 0, b = 1, c;
		System.out.println("Introduce el número de términos de la serie de Fibonacci a mostrar:");
		n = scan.nextInt();
		System.out.print("Los " + n + " primeros términos de la serie de Fibonacci son: " + a + ", " + b);
		for (int i = 2; i < n; i++) {
			c = a + b;
			System.out.print(", " + c);
			b = c;
			}
		System.out.println(".");
		}
}
