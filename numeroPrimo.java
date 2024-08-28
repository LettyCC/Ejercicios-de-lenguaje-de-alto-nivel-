import java.util.InputMismatchException;
import java.util.Scanner;

public class esPrimo {

    // Entrada: un número entero y positivo
    public static boolean esPrimo(int numero) {
        // Proceso: se verifica si el número es primo
        if (numero < 2) {
            return false;
        }
        for (int i = 2; i < numero; i++) {
            if (numero % i == 0) {
                return false;
            }
        }
        // Salida: se retorna true si el número es primo
        return true;
    }

    // Función que valida si el número ingresado es primo
    public static void validarNumeroPrimo() {
        Scanner sc = new Scanner(System.in);
        int numero = -1; // Inicialización de la variable fuera del bucle
        // para que sea accesible en todo el método

        // Entrada: un número entero y positivo
        while (true) {
            try {
                System.out.println("Por favor ingrese un número: ");
                numero = sc.nextInt(); // Asignación del valor a la variable
                // Proceso: se verifica si el número es positivo
                if (numero >= 0) {
                    break; // Salir del bucle si se ingresa un número válido
                } else {
                    System.out.println("Ingrese un número positivo");
                }
            } catch (InputMismatchException e) {
                System.out.println("Ingrese un número entero");
                sc.next(); // Limpiar el valor incorrecto del scanner
            }
        }

        // Salida: se imprime si el número es primo o no
        if (esPrimo(numero)) {
            System.out.println(numero + " es primo");
        } else {
            System.out.println(numero + " no es primo");
        }
    }

    // Método principal que llama a la función validarNumeroPrimo
    public static void main(String[] args) {

        validarNumeroPrimo();
    }
}
