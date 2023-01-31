package com.edu;

import java.util.Scanner;

// Realiza un método que reciba una hora por parámetro y que muestre luego buenos
// días, buenas tardes o buenas noches según corresponda. Se utilizarán los tramos
// de 6 a 12, de 13 a 20 y de 21 a 5, respectivamente, sólo teniendo en cuenta el valor
// de las horas.

public class Ejercicio_5 {
	public static void main(String[] args) {
		Ejercicio_5 sc = new Ejercicio_5();
		sc.getGreeting(15);
	}
	public static void getGreeting(int hour) {
		String greeting;
	    if (hour >= 6 && hour <= 12) {
	       System.out.println("Buenos días");
	    }else if (hour >= 13 && hour <= 20) {
	    	System.out.println("Buenas Tardes");
	    }else {
	    	System.out.println("Buenas Noches");
	    }
	}
}


