package com.edu;

import java.util.Scanner;

// Realizar un método llamado calcularAreaCirculo que devuelva el área de un círculo
// y otro llamado calcularLongitudCirculo que devuelva su longitud

public class Ejercicio_18 {
	  public static double calcularAreaCirculo(double radio) {
	    return Math.PI * Math.pow(radio, 2);
	  }
	  
	  public static double calcularLongitudCirculo(double radio) {
	    return 2 * Math.PI * radio;
	  }
	  
	  public static void main(String[] args) {
	    double radio = 5.0;
	    
	    System.out.println("Área del círculo con radio " + radio + ": " + calcularAreaCirculo(radio));
	    System.out.println("Longitud del círculo con radio " + radio + ": " + calcularLongitudCirculo(radio));
	  }
	}
