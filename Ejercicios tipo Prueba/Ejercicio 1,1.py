def normalizar_nota(nota):
    return nota / 10 if nota > 10 else nota

ea1 = normalizar_nota(float(input("Ingrese la nota de la ea1: ")))
ea2 = normalizar_nota(float(input("Ingrese la nota de la ea2: ")))
ea3 = normalizar_nota(float(input("Ingrese la nota de la ea3: ")))
examen = normalizar_nota(float(input("Ingrese la nota del examen: ")))

promedio_presentacion = (ea1 * 0.3 + ea2 * 0.4 + ea3 * 0.3)
promedio_final = (promedio_presentacion * 0.6 + examen * 0.4)

print("El promedio de presentación final es: ", round(promedio_presentacion, 1))
print("El promedio final es: ", round(promedio_final, 1))