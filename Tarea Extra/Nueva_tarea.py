#desarrolla im progra,a em python que permita calcular los beneficios en becas de alimentacion para los estudiantes de primer año 
#segun sus condiciones academicas y socioeconomicas.
#codiciones academicas: promedio final del colegio o liceo
#condiciones socioeconomicas: Decil al que pertenece su grupo familiar (10 deciles en total).
#beneficios: La siguiente tabla muestra los beneficios segun las condiciones recien mencionadas.
#Condicion Academica    Condicion Socioeconomica	    Beneficio en beca de alimentacion
#Promedio mayor a 6.5        Decil 1 o 2		      $200.000 pesos de beca de alimentacion
#Promedio mayor a 6.5        Decil 3 o 4		      $150.000 pesos de beca de alimentacion
#5.5 < Promedio <= 6.5       Decil 1 o 2		      $120.000 pesos de beca de alimentacion
#5.5 < Promedio <= 6.5       Decil 3 o 4		      $100.000 pesos de beca de alimentacion
#ademas, por el solo hecho de pertenecer al decil 1,2 o 3 tiene un beneficio de $50.000 pesos adicionales
#si ademas el promedio es mayor o igual a 6.0 y pertenece a estos deciles, se le entrega un beneficio adicional de $30.000 pesos.
#Valores Base:
#Beca segun condiciones academicas y socioeconomicas:
#El programa debe calcular el valor de la beca de alimentacion y mostrar el resultado al usuario.
#Menu Base :O
# Programa para calcular los beneficios en becas de alimentación para estudiantes de primer año
# según sus condiciones académicas y socioeconómicas.

print("Bienvenido al sistema de becas de alimentación")
print("1. Calcular beca de alimentación")
print("2. Salir")

opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    promedio = float(input("Ingrese su promedio final del colegio o liceo: "))

    if promedio < 0 or promedio > 7:
        print("Error: El promedio debe estar entre 0 y 7.")
        exit()

    beca_alimentacion = 0

    print("Menú de deciles")
    print("1. Decil 1")
    print("2. Decil 2")
    print("3. Decil 3")
    print("4. Decil 4")
    print("5. Decil 5")
    print("6. Decil 6")
    print("7. Decil 7")
    print("8. Decil 8")
    print("9. Decil 9")
    print("10. Decil 10")

    decil = int(input("Ingrese su decil (1 al 10): "))

    if decil < 1 or decil > 10:
        print("Error: El decil debe estar entre 1 y 10.")
        exit()

    if promedio > 6.5:
        if decil in [1, 2]:
            beca_alimentacion = 200000
        elif decil in [3, 4]:
            beca_alimentacion = 150000
    elif 5.5 < promedio <= 6.5:
        if decil in [1, 2]:
            beca_alimentacion = 120000
        elif decil in [3, 4]:
            beca_alimentacion = 100000

    if decil in [1, 2, 3]:
        beca_alimentacion += 50000

    if promedio >= 6.0 and decil in [1, 2, 3]:
        beca_alimentacion += 30000

    print(f"Su beca de alimentación es: ${beca_alimentacion} pesos")

elif opcion == 2:
    print("Gracias por usar el sistema de becas de alimentación")
else:
    print("Opción inválida")
    exit()