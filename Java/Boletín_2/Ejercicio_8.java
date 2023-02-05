package Boletín_2;

import java.util.Scanner;


// Realiza un método llamado toBinary que reciba un número decimal como
// argumento y devuelva un String con el número binario correspondiente.
public class Ejercicio_8 {
	public static String toBinary(int decimal) {
		  String binary = "";
		  while (decimal > 0) {
		    binary = (decimal % 2) + binary;
		    decimal = decimal / 2;
		  }
		  return binary;
	}
	public static void main(String[] args) {
		  int decimal = 199999;
		  System.out.println(toBinary(decimal));
	}
}		


