package Boletín_2;

import java.util.Scanner;


// Realizar un método llamado esMultiplo que recibirá dos números y devuelva True si
// el primer número es múltiplo del segundo.


public class Ejercicio_5 {
	  public static boolean esMultiplo(int a, int b) {
		  return a % b == 0;
	  }
	  public static void main(String[] args) {
		    int num1 = 8;
		    int num2 = 15;
		    if (esMultiplo(num1, num2)) {
		      System.out.println(num1 + " es múltiplo de " + num2);
		    } else {
		      System.out.println(num1 + " no es múltiplo de " + num2);
		    }
	  }
}


