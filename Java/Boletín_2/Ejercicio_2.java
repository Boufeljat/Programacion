package Boletín_2;
import java.util.Scanner;

// Realiza un programa que pida un número por teclado y que después muestre ese
// número al revés.


public class Ejercicio_2 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Introduce un número: ");
    int num = sc.nextInt();
    sc.close();
    StringBuilder sb = new StringBuilder();
    sb.append(num);
    System.out.println("Número al revés: " + sb.reverse().toString());
  }
}

