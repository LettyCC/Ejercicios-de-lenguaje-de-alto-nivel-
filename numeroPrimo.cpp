#include <iostream>

// Entrada del programa y validación si el número es primo o no
bool esPrimo(int numero)
{
    // Proceso: Si el número es menor a 2, no es primo
    if (numero < 2)
    {
        return false;
    }
    // Bucle que recorre los números desde 2 hasta el número ingresado,
    // si el número es divisible por algún número en ese rango, no es primo
    for (int i = 2; i < numero; i++)
    {
        if (numero % i == 0)
        {
            return false;
        }
    }
    // Salida: Si no se cumple ninguna de las condiciones anteriores, el número es primo
    return true;
}

// Función que valida si el número ingresado es un entero positivo y entero
void validarNumeroPrimo()
{
    // Un número entero positivo y entero
    int numero;
    //Entrada: Se pide un número entero positivo
    while (true)
    {
        std::cout << "Por favor ingrese un número: ";
        std::cin >> numero;
        // Proceso: Si el número es positivo, se sale del bucle
        if (numero >= 0)
        {
            break;
        }
        else
        {
            std::cout << "Ingrese un número positivo" << std::endl;
        }
    }
    // Salida: Se imprime si el número es primo o no
    if (esPrimo(numero))
    {
        std::cout << numero << " es primo" << std::endl;
    }
    else
    {
        std::cout << numero << " no es primo" << std::endl;
    }
}

int main()
{
    // Llamada a la función
    validarNumeroPrimo();
    return 0;
}
