ARANCEL_BASE = 1_800_000
MATRICULA_BASE = 90_000

while True:
    try:
        promedio = float(input("Ingrese su promedio (1.0 a 7.0): "))
        if 1.0 <= promedio <= 7.0:
            break
        else:
            print("El promedio debe estar entre 1.0 y 7.0.")
    except ValueError:
        print("Por favor, ingrese un número válido.")

while True:
    try:
        quintil = int(input("Ingrese su quintil (1 a 5): "))
        if 1 <= quintil <= 5:
            break
        else:
            print("El quintil debe estar entre 1 y 5.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

descuento_arancel = 0.0
descuento_matricula = 0.0

if promedio > 6.0:
    if quintil in [1, 2]:
        descuento_arancel = 0.20
    elif quintil in [3, 4]:
        descuento_arancel = 0.15
elif 5.0 < promedio <= 6.0:
    if quintil in [1, 2]:
        descuento_arancel = 0.13
    elif quintil in [3, 4]:
        descuento_arancel = 0.10

if quintil in [1, 2, 3]:
    descuento_matricula = 0.10
    if promedio >= 5.5:
        descuento_matricula += 0.05

arancel_final = ARANCEL_BASE * (1 - descuento_arancel)
matricula_final = MATRICULA_BASE * (1 - descuento_matricula)

print("\n--- Resultados ---")
print(f"Descuento aplicado al arancel: {descuento_arancel*100:.0f}%")
print(f"Descuento aplicado a la matrícula: {descuento_matricula*100:.0f}%")
print(f"Valor final del arancel: ${arancel_final:,.0f}")
print(f"Valor final de la matrícula: ${matricula_final:,.0f}")
