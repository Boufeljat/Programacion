package com.edu;

import java.util.Scanner;

// Codifica las siguientes secuencias numéricas haciendo uso de estructuras: i) for, ii)
// while, iii) do-while en cada una de ellas:
//    	a. Crea un método que muestre los números del 1 al 100
//		b. Repite el ejercicio anterior, pero en formato descendente, es decir, del 100 al 1.
// 		c. Crea un programa que calcule y escriba los números múltiplos de 5 de 0 a 100.
// 		d. Escribe los números del 320 al 160, contando de 20 en 20 hacia atrás

public class Ejercicio_7 {
	public static void main(String[] args) {
		Ejercicio_7 sc = new Ejercicio_7();
		sc.MostrarNumerosFor(100);
		sc.MostrarNumerosWhile(100);
		sc.NumerosMultiplosde5(100);
		sc.mostrarNumerosAtrasPara(360, 160, 20);
	}
	public static void MostrarNumerosFor(int n) {
		for (int i = 1; i <= n; i++) {
		     System.out.println(i);
		}
	}
	public static void MostrarNumerosWhile(int n) {
		int i = n;
		while (i >= 1) {
	         System.out.println(i);
	         i--;
	    }
	}
	public static void NumerosMultiplosde5(int n) {
	    int i = 0;
	    do {
		    if (i % 5 == 0) {
		         System.out.println(i);
		       }
		         i++;
		    }while (i <= n);
	}
	public static void mostrarNumerosAtrasPara(int start, int end, int step) {
	   for (int i = start; i >= end; i -= step) {
	      System.out.println(i);
	   }
	}
}
