package com.edu;

import java.util.Scanner;

//Programar un sistema de calefacción-refrigeración que compruebe en función del
//día y el mes, la estación en la que estamos y dependiendo de la estación programe
//la temperatura: Invierno→19º, Primavera→20º, Verano→24º, Otoño→19º.
//El método deberá recibir como parámetro el mes y el día actual y devolver los
//grados a los que deberemos programar el sistema

public class Ejercicio_6 {
	public static void main(String[] args) {
		Ejercicio_6 sc = new Ejercicio_6();
		sc.getTemperature(12, 10);
	}
	public static void getTemperature(int month, int day) {
		if (month == 3 && day >= 20 || month == 4 || month == 5 || month == 6 && day <= 20) {
		    System.out.println("20º");
		}else if (month == 6 && day >= 21 || month == 7 || month == 8 || month == 9 && day <= 23) {
			System.out.println("24º");
		}else {
			System.out.println("19º");
		}
	}
}