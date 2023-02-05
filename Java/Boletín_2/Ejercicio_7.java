package Boletín_2;

// Realizar un método llamado segundosEntre que recibirá seis valores enteros, los
// tres primeros representarán la hora, minuto y segundos de la primera hora y los
// otros tres de la segunda hora. Se deberá devolver el número de segundos que hay
// entre la primera hora y la segunda (el valor debe ser siempre en positivo). Si los
// datos no son correctos se deberá devolver -1000.

// Primera Hora 
// num1 = Hora1
// num2 = Minutos1
// num3 = Segundos1
// 08:21:30 Primera Hora
// 08:21:50 Segunda Hora
// En este caso número de segundos que hay entre la primera hora y la segunda son: 20 Segundos

//Segunda Hora 
//num4 = Hora2
//num5 = Minutos2
//num6 = Segundos2 

public class Ejercicio_7 {
    public static int segundosEntre(int hora1, int minuto1, int segundo1, int hora2, int minuto2, int segundo2) {
    	if (hora1 >= 0 && hora1 < 24 && minuto1 >= 0 && minuto1 < 60 && segundo1 >= 0 && segundo1 < 60
            && hora2 >= 0 && hora2 < 24 && minuto2 >= 0 && minuto2 < 60 && segundo2 >= 0 && segundo2 < 60) {
            int segundos1 = (hora1 * 3600) + (minuto1 * 60) + segundo1;
            int segundos2 = (hora2 * 3600) + (minuto2 * 60) + segundo2;
            return Math.abs(segundos2 - segundos1);
        } else {
            return -1000;
        }
    }

    public static void main(String[] args) {
        int hora1 = 10;
        int minuto1 = 30;
        int segundo1 = 15;
        int hora2 = 12;
        int minuto2 = 58;
        int segundo2 = 20;

        int segundos = segundosEntre(hora1, minuto1, segundo1, hora2, minuto2, segundo2);
        if (segundos != -1000) {
            System.out.println("El número de segundos entre las dos horas es: " + segundos);
        } else {
            System.out.println("Los datos introducidos no son correctos");
        }
    }
}

