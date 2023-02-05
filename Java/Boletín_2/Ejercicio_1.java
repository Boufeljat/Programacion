package Boletín_2;

import java.util.Scanner;



// Realizar un método llamado numeroSolucionesEcuacionSegundoGrado que reciba
// los coeficientes de una ecuación de segundo grado y devuelva el número de
// soluciones que tiene. Si los argumentos no son válidos (el primer coeficiente tiene
// que ser distinto de cero) debe devolver un -1.

// ax^2 + bx + c = 0 Ecuacuón de segundo grado
// Las coeficientes de este ecuación son: a + b
// a != 0
// 4x^2 + 5x + 6 = 0   
// 	a= 4
// 	b= 5
// 	c= 6

public class Ejercicio_1 {
	public static void main(String[] args) {
		Ejercicio_1 sc = new Ejercicio_1();
		sc.numeroSolucionesEcuacionSegundoGrado(4, 4, -2);
	}
	public static void numeroSolucionesEcuacionSegundoGrado(double a, double b, double c) {
		if (a == 0) {
			System.out.println(-1);
			}
		double discriminante = (b * b) - 4 * a * c;
		if (discriminante > 0) {
			System.out.println("El número de soluciones que tiene esta ecuación son: 2");
		}else if (discriminante == 0) {
			System.out.println("El número de soluciones que tiene esta ecuación son: 1");
		} else {
			System.out.println("El número de soluciones que tiene esta ecuación son: 0");
		}
	}
}
