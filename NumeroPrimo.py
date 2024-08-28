# Este programa valida si un número es primo o no
# Utiliza funciones/métodos, bucles y estructuras condicionales.


#Entrada: Un número entero positivo y entero
def esPrimo(numero): # Función que recibe un número y retorna
    if numero < 2:  # si el numero es menor a 2, no es primo
        return False
    # Proceso: Bucle que recorre los números desde 2 hasta el número ingresado,
    # si el número es divisible por algún número en ese rango, no es primo
    for i in range(2, numero):
        if numero % i == 0:
            return False
    #Salida: Si el número no es divisible por ningún número en el rango, es primo
    return True

# Función que valida si el número ingresado es un entero positivo y entero
def validarNumeroPrimo():
    # Entrada: Un número entero positivo y entero
    while True:
        try:
            numero = int(input("Por favor ingrese un número: "))
        #Proceso: Si el número es menor a 0, se pide un número positivo y si no es un número entero, se pide un número entero
            if numero >= 0:
                break
            else:
                print("Ingrese un número positivo")
        except ValueError:
            print("Ingrese un número entero")
    #Salida: Se imprime si el númeroS es primo o no
    if esPrimo(numero):
        print(f"{numero} es primo")
    else:
        print(f"{numero} no es primo")
#Llamada a la función
validarNumeroPrimo()
