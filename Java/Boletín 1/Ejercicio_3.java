package com.edu;

import java.util.Scanner;

// Escribir un método que reciba un carácter y devuelva el tipo de carácter que es.
// Debe devolver una de los siguientes mensajes según corresponda:
// ◦ Letra mayúscula
// ◦ Letra minúscula
// ◦ Dígito entre 0 y 9
// ◦ Signo de puntuación
// ◦ Espacio en blanco
// ◦ Paréntesis () o llaves {}
// ◦ Otro carácter

public class Ejercicio_3 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		char c = '}';
		if (Character.isLowerCase(c)) {
			System.out.println("Letra Minúscula");
		}else if (Character.isUpperCase(c)) {
			System.out.println("Letra Mayúscula");
		}else if (Character.isDigit(c)) {
			System.out.println("Dígito entre 0 y 9");
		}else if (c == ',' || c == '.' || c == ':' || c == ';' || c == '?' || c == '!') {
			System.out.println("Signo de puntuación");
		}else if (c == '(' || c == ')' || c == '{' || c == '}') {
			System.out.println("Paréntesis () o llaves {}");
		}else {
			System.out.println("Otro carácter");
		}
	}
}
