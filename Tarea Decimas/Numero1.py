#Ejercicio 1: Variables y Validación de Acceso

#Tema: Variables (strings)

#Descripción: Crea un programa que simule el acceso a una aplicación de streaming. El programa debe:

#1. Solicitar nombre de usuario y contraseña
#2. Comparar con credenciales predefinidas
#3. Mostrar un mensaje de bienvenida personalizado si las credenciales son correctas
#4. Mostrar un mensaje de error si las credenciales son incorrectas
#5. Si el usuario está registrado pero la contraseña es incorrecta, dar una pista sobre la contraseña (primera letra)

Usuario_C = "Maty"
Contra_C = "1234"

# Solicitar nombre de usuario y contraseña
Usuario = input("Ingrese su nombre de usuario de Twitch: ")
Contra = input("Ingrese su contraseña de Twitch: ")

# Comparar con credenciales predefinidas
if Usuario == Usuario_C and Contra == Contra_C:
    print(f"Bienvenido {Usuario} a su cuenta de Twitch¡!")
elif Usuario == Usuario_C and Contra != Contra_C:
    print("Contraseña incorrecta. Pista: la primera letra de la contraseña es:", Contra_C[0])
else:
    print("Usuario no registrado.")
# Fin del programa
