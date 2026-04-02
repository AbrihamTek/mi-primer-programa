print("💰 Calculadora de gastos")

total = 0

while True:
    gasto = input("Ingresa un gasto (o escribe 'salir'): ")

    if gasto == "salir":
        break

    try:
        gasto = int(gasto)
        total = total + gasto

        print("Total actual:", total)

        if total > 10000:
            print("⚠️ Estás gastando mucho")

    except:
        print("⚠️ Eso no es un número válido")

print("Tu gasto total fue:", total)


