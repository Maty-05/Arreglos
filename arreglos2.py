
playlistdelCurso = [
    "Beat-it.mp3",
    "Loba.mp3",
    "15B.mp3",
    "Diva virtual.mp3",
    "Pokemon johtho.mp3",
    "Pokemon kanto.mp3",
]

print(playlistdelCurso)
print("##########")
print("##########")
print(playlistdelCurso[3])

tamaño = len(playlistdelCurso)
print("El tamaño del arreglo es:", tamaño)


print("#####---La ultima cancion es:---#####")
print(playlistdelCurso[tamaño - 1])

print("imprimir todas las letras de una palabra")
palabra = "GirafariG"
for letra in palabra:
    print(letra)
print("################")
print("################")
for i in range(len(palabra)):
    print(palabra[i])


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
