import random

vida_heroe = 200
vida_monstruo = 100

while vida_heroe > 0 and vida_monstruo > 0:
    # El héroe ataca
    daño_heroe = random.randint(60, 200)
    vida_monstruo -= daño_heroe
    print("🧙‍♂️ El héroe ataca y hace", daño_heroe, "de daño.")

    # El monstruo ataca
    daño_monstruo = random.randint(80, 100)
    vida_heroe -= daño_monstruo
    print("👹 El monstruo ataca y hace", daño_monstruo, "de daño.")

    # Mostrar vidas restantes
    print("💚 Vida del héroe:", vida_heroe)
    print("❤️ Vida del monstruo:", vida_monstruo)

    # Evaluar resultado
    if vida_heroe <= 0 and vida_monstruo <= 0:
        print("😱 ¡Ambos han caído al mismo tiempo!")
        break
    elif vida_heroe <= 0:
        print("💀 El héroe ha caído. El monstruo gana.")
        break
    elif vida_monstruo <= 0:
        print("🏆 El héroe ha vencido al monstruo.")
        break
    else:
        print("⚔️ ¡Ambos siguen de pie! La batalla continúa...")

    if daño_heroe >= 100:
        print("El monstruo ha sido OneShooteado")
