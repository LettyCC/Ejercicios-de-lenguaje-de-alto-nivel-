# El Programa que permite gestionar las notas de los estudiantes, ingresando 3 calificaciones por estudiante 
# y calculando el promedio de las mismas.

# Función para calcular el promedio de las calificaciones.
def calcularPromedio(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

#Funcion para gestionar las notas de los estudiantes

def sistemaGestionNotas():
    #Inicio
    print("======Bienvenido a nuestro Sistema de gestión de notas======")
#Entrada
# Se solicita al usuario que ingrese el número de estudiantes.
    numeroEstudiantes = int(input("Por favor ingrese el número de estudiantes: "))
    listaEstudiante = ""
    # Ciclo para ingresar los datos de cada estudiante.
    for i in range(numeroEstudiantes): 
        nombreEstudiante = input("Por favor ingrese el nombre del estudiante: ")   
        nota1 = float(input("Ingrese la primera calificación del estudiante: "))
        nota2 = float(input("Ingrese la segunda calificación del estudiante: "))
        nota3 = float(input("Ingrese la tercera calificación del estudiante: "))
        promedioTotal = calcularPromedio(nota1, nota2, nota3)
        #Proceso
        if promedioTotal >= 60:
            estado = "El estudiante está aprobado"
        else:
            estado = "El estudiante está reprobado"
        # Almacenamiento de datos del estudiante
        listaEstudiante += f"Nombre: {nombreEstudiante}, Promedio: {promedioTotal:.2f}, Estado: {estado}\n"
    #Salida
    print("Listado de estudiantes:")
    print(listaEstudiante)
    print("======Gracias por usar nuestro programa ======")
    
# Llamada a la función

sistemaGestionNotas()
