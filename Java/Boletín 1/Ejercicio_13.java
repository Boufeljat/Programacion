package com.edu;

import java.util.Scanner;

// Programa que reciba 10 números y nos indique el valor máximo y mínimo.

public class Ejercicio_13 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int num, min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
		System.out.println("Introduce 10 números:");
		for (int i = 0; i < 10; i++) {
			num = scan.nextInt();
			if (num < min) {
				min = num;
				}
			if (num > max) {
				max = num;
				}
			}
		System.out.println("El número mínimo introducido es " + min);
		System.out.println("El número máximo introducido es " + max);
		}
}
