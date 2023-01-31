package com.edu;

import java.util.Scanner;

// Realiza un programa que vaya pidiendo números hasta que se introduzca un
// número negativo y nos diga cuántos números se han introducido, la media de los
// impares y el mayor de los pares. El número negativo sólo se utiliza para indicar el
// final de la introducción de datos pero no se incluye en el cómputo.


public class Ejercicio_14 {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int num, count = 0, sumImpares = 0, countImpares = 0, mayorPar = Integer.MIN_VALUE;
		System.out.println("Introduce números (introduce un número negativo para salir):");
		do {
			num = scan.nextInt();
			if (num >= 0) {
				count++;
				if (num % 2 != 0) {
					sumImpares += num;
					countImpares++;
					}else if (num > mayorPar) {
						mayorPar = num;
						}
				}
			} while (num >= 0);
		System.out.println("Se han introducido " + count + " números.");
		if (countImpares > 0) {
			System.out.println("La media de los números impares es " + (double) sumImpares / countImpares + ".");
			} else {
				System.out.println("No se han introducido números impares.");
				}
		if (mayorPar != Integer.MIN_VALUE) {
			System.out.println("El mayor de los números pares es " + mayorPar + ".");
			} else {
				System.out.println("No se han introducido números pares.");
				}
		}
}
