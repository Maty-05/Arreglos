def transformar_nota(nota):
    if nota == 8 or nota == 9:
        print("Nota inválida")
    exit()
    if nota > 7:
        return round(nota / 10, 1)
    return float(nota)

ea1 = transformar_nota(float(input("Ingrese la nota de la EA1: ")))
ea2 = transformar_nota(float(input("Ingrese la nota de la EA2: ")))
ea3 = transformar_nota(float(input("Ingrese la nota de la EA3: ")))

prom_presentacion = round((ea1 * 0.3 + ea2 * 0.4 + ea3 * 0.3), 1)
print(f"El promedio de presentación final es: {prom_presentacion}")

examen = transformar_nota(float(input("Ingrese la nota del examen: ")))

promedio_final = round((prom_presentacion * 0.6 + examen * 0.4), 1)
print(f"El promedio final es: {promedio_final}")