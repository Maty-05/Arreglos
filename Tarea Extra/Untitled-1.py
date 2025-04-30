usuario_correcto = "UsuarioDuoc"
contraseña_correcta = "RutUsuario"

usuario_usado = input("Ingrese su usuario: ")
contraseña_usada = input("Ingrese su contraseña: ")

if usuario_usado == usuario_correcto and contraseña_usada == contraseña_correcta:
    print("Bienvenido al sistema")
else:
    print("Usuario o contraseña incorrectos")
    print("Acceso denegado")
    print("Por favor, intente nuevamente")