# Ejercicio Personal de Matematicas:
# Agustina y julio van a compartir un premio de $20.650.000 en forma proporcioal al dinero que 
# cada uno invitrtio en comprar el billete de loteria premiado. 
# Si agustina aporta $650 y Julio aporto $450 ¿Que monto del premio corresponde recibir a julio?

premio_total = 20650000
aporte_agustina = 650
aporte_julio = 450

total_aporte = aporte_agustina + aporte_julio

proporcion_julio = aporte_julio / total_aporte
premio_julio = premio_total * proporcion_julio

print(f"El monto del premio que corresponde a Julio es: ${premio_julio:,.0f}")

