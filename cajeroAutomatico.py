'''
El programa simula a un cajero automático, permitiendo al usuario realizar las siguientes operaciones:
- Consultar saldo
- Depositar dinero
- Retirar dinero
- Salir
Para ello, se solicita al usuario que ingrese su PIN
En caso de ser correcto, se muestra un menú con las opciones mencionadas anteriormente.
'''
# Función para consultar el saldo
def consultarSaldo(saldo):
    #Salida
    print(f"Su saldo actual es de: ${saldo}")

# Función para depositar dinero   
def depositarDinero(saldo):
    #Entrada
    cantidad = float(input("Por favor, ingrese la cantidad que desea depositar: $"))
    if cantidad <= 0:
        #Salida
        print("La cantidad ingresada no es válida.")
    else:
        saldo += cantidad
        #Salida
    print(f"Usted ha depositado ${cantidad} en su cuenta.")
    return saldo

# Función para retirar dinero
def retirarDinero(saldo):
    #Entrada
    cantidad = float(input("Por favor, ingrese la cantidad que desea retirar: $"))
    if cantidad > saldo:
        #Salida
        print("No tiene suficientes fondos para realizar esta operación.")
    else:
        saldo -= cantidad
        #Salida
        print(f"Usted ha retirado ${cantidad} de su cuenta.")
    return saldo

# Función principal para el cajero automático

def cajeroAutomatico():
    saldo = 1500.00  # Saldo inicial 
    pinCorrecto = 2497 
    intentos = 0
    maxIntentos = 3  # Máximo número de intentos
    #Inicio
    print("Bienvenido a nuestro cajero automático.")
    
    # Bucle para verificar el PIN
    while intentos < maxIntentos:
        #Entrada
        pin = int(input("Por favor, ingrese su PIN: "))
        if pin == pinCorrecto:
            #Salida
            print(" El PIN es correcto. Bienvenido a nuestro cajero automático.")
            while True:
                print("Por favor, seleccione una opción:")
                print("1. Consultar saldo")
                print("2. Depositar dinero")
                print("3. Retirar dinero")
                print("4. Salir")
                #Entrada
                opcion = int(input("Opción: "))

                # Proceso
                if opcion == 1:
                    consultarSaldo(saldo)
                elif opcion == 2:
                    saldo = depositarDinero(saldo)
                elif opcion == 3:
                    saldo = retirarDinero(saldo)
                elif opcion == 4:
                    print("Gracias por utilizar nuestro cajero automático.")
                    return  # Termina la ejecución del programa
                else:
                    #Salida
                    print("La opción ingresada no es válida. Por favor, intente de nuevo.")
            break
        else:
            intentos += 1
            #Salida
            print(f"PIN incorrecto. Le quedan {maxIntentos - intentos} intentos.")
    # Salida
    if intentos == maxIntentos:
        print("Ha excedido el número de intentos permitidos. Su cuenta ha sido bloqueada.")

# Llamada a la función principal
cajeroAutomatico()
