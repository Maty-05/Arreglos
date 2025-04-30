#Ejercicio 5: Listas y Organizador de Biblioteca Digital

# Tema: Listas y manipulación de colecciones

#Descripción: Crea un programa que ayude a organizar una pequeña biblioteca digital de
#libros:
#1. Define una lista con al menos 5 libros (títulos como strings)
#2. Permite al usuario:
#   Ver todos los libros
#   Buscar un libro por nombre (indicar si existe o no)
#   Agregar un nuevo libro (verificando que no exista ya)
#   Eliminar un libro (verificando que exista)
#3. Utiliza comparaciones con if para las verificaciones
#4. Muestra mensajes apropiados en cada operación
#5. Si la biblioteca supera los 10 libros, mostrar un mensaje indicando que la versión gratuita está llena

biblioteca = ["Luna de Pluton", "One Piece", "El principito", "Don Quijote", "Moby Dick"]

def mostrar_libros():
    print("\nLista de libros:")
    for libro in biblioteca:
        print(f"- {libro}")

def buscar_libro():
    libro = input("\nIngrese el nombre del libro que desea buscar: ")
    if libro in biblioteca:
        print(f"El libro '{libro}' está en la biblioteca.")
    else:
        print(f"El libro '{libro}' no está en la biblioteca.")

def agregar_libro():
    libro = input("\nIngrese el nombre del libro que desea agregar: ")
    if libro in biblioteca:
        print(f"El libro '{libro}' ya existe en la biblioteca.")
    else:
        biblioteca.append(libro)
        print(f"El libro '{libro}' ha sido agregado a la biblioteca.")
        if len(biblioteca) > 10:
            print("La biblioteca ha superado los 10 libros. La versión gratuita está llena.")

def eliminar_libro():
    libro = input("\nIngrese el nombre del libro que desea eliminar: ")
    if libro in biblioteca:
        biblioteca.remove(libro)
        print(f"El libro '{libro}' ha sido eliminado de la biblioteca.")
    else:
        print(f"El libro '{libro}' no está en la biblioteca.")

while True:
    print("\n--- Menú de Biblioteca Digital ---")
    print("1. Ver todos los libros")
    print("2. Buscar un libro")
    print("3. Agregar un libro")
    print("4. Eliminar un libro")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        mostrar_libros()
    elif opcion == "2":
        buscar_libro()
    elif opcion == "3":
        agregar_libro()
    elif opcion == "4":
        eliminar_libro()
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo :D.")