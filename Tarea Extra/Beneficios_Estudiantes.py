#Desarrolle un programa en python que permita calcular los nemeficios a los estudiantes de primer año segun sus condiciones academicas y socioeconomicas. 
# Las condiciones academicas estan basadas en el promedio final con el que salieron del colegio o liceo. Las condiciones socioeconomicas
#estan basadas segun el quintil al que pertenece su grupo familiar (5 quintiles en total). La tabla siguiente muestra el beneficio según 
#las condiciones recien mencionadas.

#Condicion Academica    Condicion Socioeconomica	Beneficio
#Promedio mayor a 6.0        Quintil 1 o 2		      20% descuento en arancel
#Promedio mayor a 6.0        Quintil 3 o 4		      15% descuento en arancel
#5.0 < Promedio <= 6.0       Quintil 1 o 2		      13% descuento en arancel
#5.0 < Promedio <= 6.0       Quintil 3 o 4		      10% descuento en arancel

#Ademas por el hecho de pertenecer al Quintil 1, 2 o 3 tiene un descuento de 10% en la matricula y si perteneciendo a esos Quintiles
#su promedio es mayor o igual a 5.5 se obtiene un 5% adicional.
#El programa debe entregar el valor final del arancel y matricula suponiendo que se le entrega el promedio y el quintil del estudiante.
#Suponga que el valor del arancel es de $1.800.000 y el valor de la matricula es de $90.000.

#Ejemplo 1:
#Ingerese promedio: 6.5
#Ingerese quintil: 1
#El valor del arancel es: $1.440.000
#El valor de la matricula es: $76.500

#Ejemplo 2:
#Ingerese promedio: 4
#Ingerese quintil: 5
#El valor del arancel es: $1.800.000
#El valor de la matricula es: $90.000

#Inicio paso a paso:
#1. Definir las variables de arancel y matricula
#2. Definir las variables de entrada y salida
#3. Definir las variables de control
#4. Definir las variables de quintil
#5. Definir las variables de descuento
#6. Definir las variables de proceso
#7. Definir las variables de resultado
#8. Definir las variables de promedio


Arancel = 1800000
Matricula = 90000

Promedio = float(input("Ingrese promedio: "))
Quintil = int(input("Ingrese quintil (1 hasta el 5): "))

Descuento_del_arancel = 0
Descuento_de_la_matricula = 0

if Promedio > 6.0:
    if Quintil in [1, 2]:
        Descuento_del_arancel = 0.20
    elif Quintil in [3, 4]:
        Descuento_del_arancel = 0.15
elif 5.0 < Promedio <= 6.0:
    if Quintil in [1, 2]:
        Descuento_del_arancel = 0.13
    elif Quintil in [3, 4]:
        Descuento_del_arancel = 0.10

if Quintil in [1, 2, 3]:
    Descuento_de_la_matricula = 0.10
    if Promedio >= 5.5:
        Descuento_de_la_matricula += 0.05

Arancel_final = Arancel * (1 - Descuento_del_arancel)
Matricula_final = Matricula * (1 - Descuento_de_la_matricula)

print(f"El valor del arancel es: ${Arancel_final:,.0f}")
print(f"El valor de la matrícula es: ${Matricula_final:,.0f}")