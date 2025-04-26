
playlistdelCurso = [
    "Beat_it",
    "Loba",
    "15B",
    "Diva_v",
    "Pokemon_j",
    "Pokemon_k",
]

print(playlistdelCurso)
print("##########")
print("##########")
print(playlistdelCurso[3])

tamaño = len(playlistdelCurso)
print("El tamaño del arreglo es:", tamaño)


print("#####---La ultima cancion es:---#####")
print(playlistdelCurso[tamaño - 1])

if input("Nombre de la canción: ") in playlistdelCurso:
    print("La cancion esta en la lista")
else:
    print("La cancion no esta en la lista")

