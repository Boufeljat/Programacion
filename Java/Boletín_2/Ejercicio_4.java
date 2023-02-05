package Boletín_2;
import java.util.Scanner;

// Elabora un programa que codifique una cadena, de tal modo que en el resultado se
// inviertan cada 2 caracteres. Los caracteres intercambiados no pueden volver a
// intercambiarse. Ejemplo:
// 		Entrada -> Hola mundo
// 		Salida -> oHalm nuod



public class Ejercicio_4 {
	  public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    System.out.print("Ingrese una cadena: ");
	    String cadena = sc.nextLine();
	    String codificacion = codificar(cadena);
	    System.out.println("La cadena codificada es: " + codificacion);
	  }
	
	  public static String codificar(String cadena) {
	    int longitud = cadena.length();
	    if (longitud <= 1) {
	      return cadena;
	    }
	    String resultado = "";
	    for (int i = 0; i < longitud; i += 2) {
	      if (i + 1 < longitud) {
	        resultado += cadena.charAt(i + 1) + "" + cadena.charAt(i);
	      } else {
	        resultado += cadena.charAt(i);
	      }
	    }
	    return resultado;
	  }
}

