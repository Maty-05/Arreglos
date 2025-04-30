#Ejercicio 2: Constantes y Calculadora de Descuentos

#Tema: Constantes y operadores

#Descripción: Desarrolla una calculadora para una tienda de ropa en línea que:

#1. Defina constantes para diferentes categorías de descuentos(DESCUENTO_ESTUDIANTE = 0.15, DESCUENTO_CLIENTE_FRECUENTE = 0.10, etc.)
#2. Solicite el precio original de un artículo
#3. Pregunte si el usuario es estudiante (s/n) y si es cliente frecuente (s/n)
#4. Aplique el descuento correspondiente (si aplican varios, usar el mayor)
#5. Muestre el precio original, el descuento aplicado y el precio final

Descuento_estudiante = 0.15
Descuento_cliente_frecuente = 0.10
Descuento_mayor = 0.20
Descuento_menor = 0.05
Descuento_ninguno = 0.0

Precio_original = float(input("Ingrese el precio original del artículo: "))

Es_estudiante = input("¿Es estudiante? (s/n): ").lower()
Es_cliente_frecuente = input("¿Es cliente frecuente? (s/n): ").lower()

Descuento_aplicado = Descuento_ninguno

if Es_estudiante == "s":
    Descuento_aplicado = max(Descuento_aplicado, Descuento_estudiante)
if Es_cliente_frecuente == "s":
    Descuento_aplicado = max(Descuento_aplicado, Descuento_cliente_frecuente)
if Precio_original > 100:
    Descuento_aplicado = max(Descuento_aplicado, Descuento_mayor)
if Precio_original < 50:
    Descuento_aplicado = max(Descuento_aplicado, Descuento_menor)

Precio_final = Precio_original * (1 - Descuento_aplicado)

print(f"Precio original: ${Precio_original:.2f}")
print(f"Descuento aplicado: {Descuento_aplicado * 100:.0f}%")
print(f"Precio final: ${Precio_final:.2f}")
