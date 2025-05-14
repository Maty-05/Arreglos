#Ejercicios usando excepciones y manejo de errores basicos sin el comando ValueError.

#Ejercicios Propuestos
#Ejercicio 1: Calculadora de Edad
#Crea un programa que:
#Pida la edad al usuario
#Valide que sea un número entero
#Calcule el año de nacimiento
#Maneje posibles errores de entrada

#Ejercicio 2: Lista de Compras Inteligente
#Desarrolla un programa que:
#Permita añadir productos a una lista
#Tenga opción de eliminar por índice
#Maneje excepciones si se intenta eliminar un índice que no existe

#Ejercicio 1 respuesta.

#Ejercicio 1: Calculadora de Edad

edad = input("Ingrese su edad: ")
for i in range(10):
    try:
        edad = int(edad)
        if edad < 0:
            raise ValueError("La edad no puede ser negativa.")
        break
    except ValueError as error:
        print(f"Error: {error}. Por favor, ingrese un número entero válido.")
        edad = input("Ingrese su edad: ")
año_actual = 2025
año_nacimiento = año_actual - edad
print(f"Usted nació en el año {año_nacimiento}.")
