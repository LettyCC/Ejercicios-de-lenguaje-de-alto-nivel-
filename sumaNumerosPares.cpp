// Suma de números pares hasta un límite dado
#include <iostream>
//Entrada: Un número entero positivo
// Método que calcula la suma de números pares hasta un límite dado
int SumaNumerosPares(int limite)
{
    int suma = 0;
    //Proceso: Suma los números pares desde 0 hasta el límite
    // Bucle que recorre los números pares desde 0 hasta el límite
    for (int i = 0; i <= limite; i += 2)
    {
        suma += i;
    }
    // Salida: Retorna la suma de los números pares
    return suma;
}

// Método que valida si el número ingresado es un entero positivo
int ValidarNumero()
{
    int numero;
    //Entrada: Un número entero positivo y entero
    while (true)
    {
        std::cout << "Por favor ingrese el número límite: ";
        std::cin >> numero;
        //Proceso: Verifica si el número ingresado es positivo
        if (numero >= 0)
        {
            break;
        }
        else
        {
            std::cout << "Ingrese un número positivo" << std::endl;
        }
    }
    return numero;
}

// Método principal que llama a los métodos anteriores
int main()
{
    int numero = ValidarNumero();
    int resultado = SumaNumerosPares(numero);
    //Salida: Muestra la suma de los números pares
    std::cout << "La suma de los números pares hasta " << numero << " es: " << resultado << std::endl;
    return 0;
}
