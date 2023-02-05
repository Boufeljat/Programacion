package Boletín_2;

// Realizar un método llamado horaMayor que recibirá seis valores enteres, los tres
// primeros representarán la hora, minuto y segundos de la primera hora y los otros
// tres de la segunda hora. Se deberá devolver un 1 si la primera hora es mayor que la
// segunda, un 2 si la segunda hora es mayor que la primera, un 0 si son iguales y un
// -1000 si los datos no son correctos.

public class Ejercicio_6{
	  public static int horaMayor(int hora1, int minuto1, int segundo1, int hora2, int minuto2, int segundo2) {
	    if (hora1 >= 0 && hora1 <= 23 && minuto1 >= 0 && minuto1 <= 59 && segundo1 >= 0 && segundo1 <= 59
	        && hora2 >= 0 && hora2 <= 23 && minuto2 >= 0 && minuto2 <= 59 && segundo2 >= 0 && segundo2 <= 59) {
	    	int SegundoHora1 = hora1 * 3600 + minuto1 * 60 + segundo1;
	    	int SegundosHora2 = hora2 * 3600 + minuto2 * 60 + segundo2;
	    	if (SegundoHora1 > SegundosHora2) {
	    		return 1;
	    	} else if (SegundoHora1 < SegundosHora2) {
	    		return 2;
	    	} else {
	    		return 0;
	    	}
	    } else {
	    	return -1000;
	    }
	  }
	  public static void main(String[] args) {
	    int hora1 = 15;
	    int minuto1 = 30;
	    int segundo1 = 45;
	    int hora2 = 12;
	    int minuto2 = 15;
	    int segundo2 = 10;
	    int resultado = horaMayor(hora1, minuto1, segundo1, hora2, minuto2, segundo2);
	    if (resultado == 1) {
	    	System.out.println("La primera hora es mayor");
	    } else if (resultado == 2) {
	    	System.out.println("La segunda hora es mayor");
	    } else if (resultado == 0) {
	    	System.out.println("Las horas son iguales");
	    } else if (resultado == -1000) {
	    	System.out.println("Los datos no son correctos");
	    }
	  }
}

