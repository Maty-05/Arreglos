#Desarrolle un programa que reciba 3 números por teclado, uno por uno, y diga: cuántos
#números son pares y cuantos impares.
#Además, debe indicar si la suma de todos los números es mayor a 100. Si lo es, debe indicar
#si la suma es par o impar.

#Ejemplo 1:
#Ingrese numero: 45
#Ingrese numero: 80
#Ingrese numero: 21
#Se ingresaron 1 números pares.
#Se ingresaron 2 números impares.
#La suma es mayor a 100.
#La suma es par.

#Ejemplo 2:
#Ingrese numero: 20
#Ingrese numero: 4
#Ingrese numero: 10
#Se ingresaron 3 números pares.
#Se ingresaron 0 números impares.
#La suma no es mayor a 100.

pares = 0
impares = 0
suma = 0

for contador in range(3):
    numero = int(input("Ingrese numero: "))
    suma += numero
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
if suma > 100:
    print("La suma es mayor a 100.")
    if suma % 2 == 0:
        print("La suma es par.")
    else:
        print("La suma es impar.")
else:
    print("La suma no es mayor a 100.")
print("Se ingresaron", pares, "números pares.")
print("Se ingresaron", impares, "números impares.")
