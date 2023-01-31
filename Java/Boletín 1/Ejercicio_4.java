package com.edu;

import java.util.Scanner;

// Calcular las calificaciones de un alumno con un método que reciba la nota de la
// parte práctica, la nota de los problemas y la parte teórica. La nota final se calcula
// según el siguiente criterio: la parte práctica vale el 10%; la parte de problemas vale
// el 50% y la parte teórica el 40%. Las notas deben estar entre 0 y 10, si no lo están,
// deberá devolver un mensaje de error.
// Realiza el método que calcule la media de tres notas y te devuelva la nota del
// boletín (insuficiente, suficiente, bien, notable o sobresaliente).

// 1- Nota de la parte práctica -- 10% 
// 2- Nota de la parte teórica -- 40%
// 3- Nota de la parte de problemas -- 50%

import java.util.Scanner;

public class Ejercicio_4 {
		public static void main(String[] args) {
			Scanner lector = new Scanner(System.in);
			System.out.print("Introduce la nota de la parte práctica: ");
			double practica = lector.nextDouble();
			System.out.print("Introduce la nota de los problemas: ");
			double problemas = lector.nextDouble();
			System.out.print("Introduce la nota de la parte teórica: ");
			double teorica = lector.nextDouble();
			double media = calcularMedia(practica, problemas, teorica);
			if (media >= 0 && media <= 10) {
			  System.out.println("La nota final es: " + media);
			  System.out.println("La calificación en el boletín es: " + calificacionBoletin(media));
			} else {
			  System.out.println("Error: las notas deben estar entre 0 y 10");
			}
			}
		public static double calcularMedia(double practica, double problemas, double teorica) {
		return (practica * 0.1) + (problemas * 0.5) + (teorica * 0.4);
		}
		
		public static String calificacionBoletin(double nota) {
			if (nota < 5) {
			return "Insuficiente";
			}else if (nota >= 5 && nota < 6) {
			return "Suficiente";
			}else if (nota >= 6 && nota < 7) {
			return "Bien";
			}else if (nota >= 7 && nota < 9) {
			return "Notable";
			}else {
			return "Sobresaliente";
			}
		}
}

