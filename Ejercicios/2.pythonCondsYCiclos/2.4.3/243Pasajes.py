# Deberás construir un programa que esta diseñado para ayudar en la venta de pasajes. 
# Inicia preguntándote cuántos pasajes deseas vender. 
totalIngresos=0
try:
    cant_pasajes=int(input("Ingrese cantidad de pasajes a vender: "))
# Luego, utiliza un proceso organizado (llamado bucle for) para pedirte el precio de cada pasaje por separado.
# Si ingresas un valor que no es un número, te indica que necesitas proporcionar un valor numérico válido.
    for i in range (cant_pasajes):
        try:
            valor_pasaje=int(input(f"Ingrese valor de pasaje n°{i+1}: "))
            totalIngresos=totalIngresos+valor_pasaje
        except ValueError:
            print("Ingrese un valor valido de pasaje")
            break
# •	Se utiliza un bucle for para iterar sobre la cantidad de pasajes.
# •	Dentro del bucle, se solicita al usuario el precio de cada pasaje y se acumula en la variable totalIngresos.
# •	Si el usuario ingresa un valor no numérico para el precio del pasaje, el programa muestra un mensaje y sale del bucle usando break.
# •	Finalmente, se imprime el total de ingresos por la venta de pasajes
except ValueError:
    print("Debe ingresar Numeros")
if totalIngresos!=0:
    print(f"El total de ingresos fue: {totalIngresos}")
else:
    print("Intentelo nuevamente")