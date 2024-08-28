import java.util.Scanner;
import java.util.InputMismatchException;

public class sumaNumerosPares {

    // Función que calcula la suma de números pares hasta un límite dado
    public static int sumaNumerosPares(int limite) {
        int suma = 0;
        // Bucle que recorre los números pares desde 0 hasta el límite
        for (int i = 0; i <= limite; i += 2) {
            suma += i;
        }
        // Retorna la suma de los números pares
        return suma;
    }

    // Función que valida si el número ingresado es un entero positivo
    public static int validarNumero() {
        int numero;
        Scanner sc = new Scanner(System.in);
        while (true) {
            try {
                System.out.print("Por favor ingrese el número límite: ");
                numero = sc.nextInt();
                if (numero >= 0) {
                    break;
                } else {
                    System.out.println("Ingrese un número positivo");
                }
            } catch (InputMismatchException e) {
                System.out.println("Ingrese un número entero");
                sc.next(); // Limpiar el buffer
            }
        }
        return numero;
    }

    // Método principal que llama a las funciones anteriores
    public static void main(String[] args) {
        int numero = validarNumero();
        int resultado = sumaNumerosPares(numero);
        System.out.println("La suma de los números pares hasta " + numero + " es: " + resultado);
    }
}
