# Construye un programa que tenga como objetivo el solo ser referente para la utilización de captura de errores por medio excepciones, el programa debe capturar error de valores, y división por cero.



while True:
    try:    
        total_cuenta=int(input("Ingresa el total de la cuenta:"))
        comensales=int(input("Ingresa la cantidad de comensales de la mesa:"))
        if comensales > 0 and total_cuenta>0:
            apagar=total_cuenta // comensales
            break
        else:
            print("debe ingresar montos validos")  
            
    except ValueError:
        print("Error: Debe ingresar digitos")
    except ZeroDivisionError:
        print("No puede haber 0 comensales en la mesa")
print(f"El valor pagar por cada comensal es de: {apagar}")    