totalIngresos = 0
cantidadPasajes = int(input("Ingrese la cantidad de pasajes a vender: "))

for i in range(1, cantidadPasajes + 1):
    try:
        precioPasaje = float(input(f"Ingrese el precio del pasaje Nro. {i}: "))
        totalIngresos += precioPasaje
    except ValueError:
        print("Ingrese un valor numérico válido para el precio del pasaje.")
        break  # Sale del bucle si se ingresa un valor no numérico.

print(f"Total de ingresos por la venta de pasajes: ${totalIngresos:.2f}")
