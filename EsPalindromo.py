print("verifica si la palabra es un palindromo")
palabra = input("Ingrese una palabra: ")
palabra = palabra.lower()
palabraReversa = ""
for i in range(len(palabra)-1, -1, -1):
    palabraReversa += palabra[i]
print("La palabra al reves es:", palabraReversa)
if palabra == palabraReversa:
    print("Es un palindromo")
else:
    print("No es un palindromo")