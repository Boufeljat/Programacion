package com.edu;

import java.util.Scanner;

// Escribe un método que reciba por parámetro el día de la semana (Lunes, Martes,Miércoles, etc) y devuelva qué asignatura toca a primera hora ese día

public class Ejercicio_2 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String dia = "Jueves";
			if (dia=="Lunes") {
				System.out.println("Programación");
			}else if(dia=="Martes") {
				System.out.println("Programación");
			}else if(dia=="Miércoles") {
				System.out.println("Programación");
			}else if(dia=="Jueves") {
				System.out.println("Formación y Orientación laboral");
			}else if(dia=="Viernes") {
				System.out.println("Programación");
			}else {
				System.out.println("El día ingesado no es válido");
			}
		}
	}

