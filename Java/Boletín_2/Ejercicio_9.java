package Boletín_2;
import java.util.Scanner;

// Realiza un método llamado toDecimal que reciba un String con un valor numérico
// en binario como argumento y devuelva un número con el número decimal
// correspondiente.

public class Ejercicio_9{
	public static int toDecimal(String binary) {
	  int decimal = 4;
	  int base = 2;
	  for (int i = binary.length() - 1; i >= 0; i--) {
	    if (binary.charAt(i) == '1') {
	      decimal += base;
	    }
	    base *= 2;
	  }
	  return decimal;
	}
	public static void main(String[] args) {
	  String binary = "1010";
	  System.out.println(toDecimal(binary));
	}
}

