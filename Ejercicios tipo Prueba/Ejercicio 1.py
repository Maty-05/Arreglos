#Desarrolle un programa en Python que permita calcular el promedio final de la asignatura de
#programación de algoritmos de un estudiante. El programa debe permitir ingresar la nota de
#la experiencia de aprendizaje 1, 2 y 3. Donde cada nota tiene una ponderación de 30%, 40%
#y 30%. Este promedio (promedio de presentación de examen) debe mostrarse por pantalla.
#Luego, el programa debe permitir ingresar la nota del Examen transversal y calcular el
#promedio final. Recuerde que el promedio final se calcula como 60% el promedio de
#presentación y 40% la nota del examen.
#Ambos promedios mostrados por pantalla deben ir redondeados con un número decimal. Siga
#el ejemplo a continuación:

#Ejemplo 1:
#Ingrese la nota de la EA1: 4
#Ingrese la nota de la EA2: 5.2
#Ingrese la nota de la EA3: 6.1
#El promedio de presentación final es: 5.1
#Ingrese la nota del examen: 4.0
#El promedio final es: 4.7

#Ejemplo 2:
#Ingrese la nota de la EA1: 1
#Ingrese la nota de la EA2: 3
#Ingrese la nota de la EA3: 5
#El promedio de presentación final es: 3.0
#Ingrese la nota del examen: 5
#El promedio final es: 3.8

ea1 = float(input("Ingrese la nota de la ea1: ")) / 10
ea2 = float(input("Ingrese la nota de la ea2: ")) / 10
ea3 = float(input("Ingrese la nota de la ea3: ")) / 10
examen = float(input("Ingrese la nota del examen: ")) / 10

promedio_presentacion = (ea1 * 0.3 + ea2 * 0.4 + ea3 * 0.3) / 1
promedio_final = (promedio_presentacion * 0.6 + examen * 0.4) / 1

print("El promedio de presentación final es: ", round(promedio_presentacion, 1))
print("El promedio final es: ", round(promedio_final, 1))

