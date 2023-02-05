package Boletín_2;

import java.util.Scanner;

// Diseña una función que, dada una cadena de entrada, comprueba si es una
// contraseña fuerte o no. Se considera que una contraseña es fuerte si contiene 8 o
// más caracteres, y entre ellos al menos hay una mayúscula, una minúscula, un signo
// de puntuación y al menos un dígito.



public class Ejercicio_3 {
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    System.out.print("Ingrese una contraseña: ");
	    String password = sc.nextLine();
	    if (esContrasenaFuerte(password)) {
	    	System.out.println("La contraseña es fuerte");
	    }else {
	    	System.out.println("La contraseña no es fuerte");
	    }
	}
	public static boolean esContrasenaFuerte(String password) {
	    int longitud = password.length();
	    if (longitud < 8) {
	      return false;
	    }
	    boolean tieneMayuscula = false;
	    boolean tieneMinuscula = false;
	    boolean tieneSignoPuntuacion = false;
	    boolean tieneDigito = false;
	    for (int i = 0; i < longitud; i++) {
	    	char c = password.charAt(i);
	    	if (Character.isUpperCase(c)) {
	    		tieneMayuscula = true;
	    	} else if (Character.isLowerCase(c)) {
	    		tieneMinuscula = true;
	    	} else if (Character.isDigit(c)) {
	    		tieneDigito = true;
	    	if (tieneMayuscula && tieneMinuscula && tieneSignoPuntuacion && tieneDigito) {
	    		return true;
	    		}
	    	}
	    return false;
	    }
	}
}



