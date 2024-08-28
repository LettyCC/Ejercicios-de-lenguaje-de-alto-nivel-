def sumaNumerosPares(límite):
    suma = 0
    for i in range(0, límite + 1, 2):
        suma += i
    return suma

def validarNumero():
    while True:
        try:
            número = int(input("Por favor ingrese el número límite: "))
            if número >= 0:
                break
            else:
                print("Ingrese un número positivo")
        except ValueError:
            print("Ingrese un número entero")
    return número

def main():
    número = validarNumero()
    resultado = sumaNumerosPares(número)
    print(f"La suma de los números pares hasta {número} es: {resultado}")

main()
