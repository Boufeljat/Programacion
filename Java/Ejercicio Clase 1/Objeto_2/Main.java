package Objeto_2;

public class Main {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double saldoInicial;
        int opcion = 0;

        System.out.print("Introduzca el saldo inicial de la cuenta: ");
        saldoInicial = sc.nextDouble();

        Cuenta cuenta = new Cuenta(saldoInicial);

        while (opcion != 4) {
            System.out.println("\nSeleccione una opción:");
            System.out.println("1. Hacer un reintegro");
            System.out.println("2. Hacer un ingreso");
            System.out.println("3. Consultar el saldo y el número de operaciones");
            System.out.println("4. Finalizar las operaciones");

            opcion = sc.nextInt();

            switch (opcion) {
                case 1:
                    System.out.print("Introduzca la cantidad a retirar: ");
                    double cantidadReintegro = sc.nextDouble();
                    cuenta.hacerReintegro(cantidadReintegro);
                    break;
                case 2:
                    System.out.print("Introduzca la cantidad a ingresar: ");
                    double cantidadIngreso = sc.nextDouble();
                    cuenta.hacerIngreso(cantidadIngreso);
                    break;
                case 3:
                    cuenta.consultarSaldo();
                    break;
                case 4:
                    System.out.println("¿Desea salir? (S/N)");
                    String respuesta = sc.next();
                    if (respuesta.equalsIgnoreCase("S")) {
                        System.out.println("El saldo final de la cuenta es: " + cuenta.getSaldo() + " euros.");
                        System.out.println("¡Hasta pronto!");
                    } else {
                        opcion = 0;
                    }
                    break;
                default:
                    System.out.println("Opción inválida.");
                    break;
            }
        }
    }
}
