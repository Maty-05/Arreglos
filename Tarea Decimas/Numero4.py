#Ejercicio 4: Aritmética y Conversor de Unidades

#Tema: Aritmética y operaciones matemáticas
#Descripción: Desarrolla un programa que convierta entre diferentes unidades de medida:
#1. Muestra un menú con las siguientes opciones:
#   Convertir de kilómetros a millas
#   Convertir de millas a kilómetros
#   Convertir de grados Celsius a Fahrenheit
#   Convertir de grados Fahrenheit a Celsius
#2. Según la opción elegida, solicita el valor a convertir
#3. Realiza los cálculos correspondientes (1 km = 0.621371 millas, °F = °C × 9/5 + 32, °C = (°F - 32) × 5/9)
#4. Si el usuario introduce un valor negativo para distancias, muestra un mensaje adecuado
#5. Para temperaturas, indica si está bajo cero, a temperatura ambiente (15-25°C) o caliente


# Mostrar menú
print("Conversor de Unidades:")
print("1. Convertir de kilómetros a millas")
print("2. Convertir de millas a kilómetros")
print("3. Convertir de grados Celsius a Fahrenheit")
print("4. Convertir de grados Fahrenheit a Celsius")

opcion = int(input("Seleccione una opción (1-4): "))

if opcion == 1:
    km = float(input("Ingrese la distancia en kilómetros: "))
    if km < 0:
        print("La distancia no puede ser negativa.")
    else:
        millas = km * 0.621371
        print(f"{km} kilómetros equivalen a {millas:.2f} millas.")

elif opcion == 2:
    millas = float(input("Ingrese la distancia en millas: "))
    if millas < 0:
        print("La distancia no puede ser negativa.")
    else:
        km = millas / 0.621371
        print(f"{millas} millas equivalen a {km:.2f} kilómetros.")

elif opcion == 3:
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = celsius * 9/5 + 32
    print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F.")
    if celsius < 0:
        print("Está bajo cero (frio).")
    elif 15 <= celsius <= 25:
        print("Temperatura ambiente (:D).")
    else:
        print("Hace calorcito.")

elif opcion == 4:
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F equivalen a {celsius:.2f}°C.")
    if celsius < 0:
        print("Está bajo cero.")
    elif 15 <= celsius <= 25:
        print("Temperatura ambiente.")
    else:
        print("Hace calor.")

else:
    print("Opción no válida. Debe ser un número entre 1 y 4.")

