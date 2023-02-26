package Objeto_1;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double longitud, ancho;
        System.out.print("Introduce la longitud del rectángulo: ");
        longitud = sc.nextDouble();
        System.out.print("Introduce el ancho del rectángulo: ");
        ancho = sc.nextDouble();
        Rectangulo rectangulo = new Rectangulo(longitud, ancho);
        double area = rectangulo.calcularArea();
        double perimetro = rectangulo.calcularPerimetro();
        System.out.println("El área del rectángulo es: " + area);
        System.out.println("El perímetro del rectángulo es: " + perimetro);
    }
}




