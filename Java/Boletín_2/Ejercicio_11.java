package Boletín_2;
import java.util.Scanner;

// Realizar un método llamado minimoComunMultiplo que reciba dos números y
// calcule el mínimo común múltiplo de dos números. Con el máximo común divisor de
// una pareja de números podemos obtener fácilmente el mínimo común múltiplo de
// dicha pareja. El mínimo común múltiplo de dos números es igual al producto de los
// números dividido entre su máximo común divisor. Por ejemplo, el máximo común
// divisor de 24 y 36 es 12, por tanto el mínimo común múltiplo de 24 y 36 es
// (24×36)/12=72.

public class Ejercicio_11{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    System.out.println("Ingrese el primer número: ");
	    int num1 = sc.nextInt();
	    System.out.println("Ingrese el segundo número: ");
	    int num2 = sc.nextInt();
	    int mcm = minimoComunMultiplo(num1, num2);
	    System.out.println("El mínimo común múltiplo de " + num1 + " y " + num2 + " es " + mcm);
	}
	
	public static int minimoComunMultiplo(int num1, int num2) {
	    int mcd = máximoComunDivisor(num1, num2);
	    int mcm = (num1 * num2) / mcd;
	    return mcm;
	}
	
	public static int máximoComunDivisor(int num1, int num2) {
	    while (num2 != 0) {
	        int temp = num2;
	        num2 = num1 % num2;
	        num1 = temp;
	    }
	    return num1;
	}
}
