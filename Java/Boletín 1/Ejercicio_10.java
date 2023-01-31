package com.edu;

import java.util.Scanner;

// Realiza un programa que sume los 100 números siguientes a un número entero y
// positivo introducido por teclado. Se debe comprobar que el dato introducido es
// correcto (que es un número positivo).

public class Ejercicio_10 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int suma = 0;
		System.out.print("Introduce un número entero positivo: ");
		int num = sc.nextInt();
		while (num <= 0) {
			System.out.println("El número introducido no es positivo.");
			System.out.print("Introduce un número entero positivo: ");
			num = sc.nextInt();
		}
		for (int i = num + 1; i <= num + 100; i++) {
			suma += i;
		}
		System.out.println("La suma de los 100 números siguientes a " + num + " es: " + suma);
	}
}
