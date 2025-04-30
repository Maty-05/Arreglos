#Ejercicio 3: Operadores y Verificador de Playlists

#Tema: Operadores lógicos y comparación

#Descripción: Crea un programa que ayude a un usuario a decidir si una canción es adecuada para su playlist basándose en criterios 
#específicos.

#1. Solicita duración de la canción en minutos (float)
#2. Solicita género musical (string)
#3. Solicita año de lanzamiento (int)
#4. Verifica si la canción cumple con los criterios para ser incluida:
#   Duración entre 2.5 y 4.5 minutos
#   Género sea "rock", "pop" o "indie" (sin distinguir mayúsculas/minúsculas)
#   Año de lanzamiento posterior a 2010
#5. El programa debe informar si la canción se incluye en la playlist y explicar por qué sí o por qué no


duracion = float(input("Ingrese la duración de la canción (en minutos, Aprox.): "))
genero = input("Ingrese el género musical de la canción: ").lower()
año = int(input("Ingrese el año de lanzamiento de la canción: "))

duracion_v = 2.5 <= duracion <= 4.5
genero_v = genero in ["rock", "pop", "indie"]
año_v = año > 2010

if duracion_v and genero_v and año_v:
    print("La canción se incluye en la playlist mencionada.")
else:
    print("La canción NO se incluye en la playlist mencionada.")
    print("Los Motivos:")
    if not duracion_v:
        print("La duración no está entre 2.5 y 4.5 minutos, como se tenia previsto.")
    if not genero_v:
        print("El género no es rock, pop ni indie :/ .")
    if not año_v:
        print("El año de lanzamiento no es posterior al año 2010.")


