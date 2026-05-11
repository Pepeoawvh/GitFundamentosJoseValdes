# El programa debe tener un menú de opciones de donde se pueda realizar el pago del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas una vez sumadas se resten al cupo disponible. 
# Las opciones disponibles deben estar construidas de la siguiente forma:
cupo_disponible=0
compra=0
deuda=100000

while True:
    try:
        print("***************************")
        print("1. Pago tarjeta de credito")
        print("2. Simulacion de compra")
        print("3. Salir")
        op=int(input("ingrese su opcion: "))
# 1.	Pago de Tarjeta de Crédito:
# a.	El usuario comienza con una deuda de $100.000
# b.	El usuario puede ingresar un monto para realizar un pago en la tarjeta de crédito.
# c.	Se debe verificar que el monto ingresado sea mayor o igual a cero.
# d.	Se debe verificar que el monto a pagar no exceda el saldo actual de la tarjeta.
# e.	Al pagar el sistema debe descontar de la deuda total
# f.	Si las verificaciones son exitosas, se realiza el pago y se actualiza el saldo de la tarjeta.
        if op==1:
            while True:
                try:
                    print("Pagando... ")
                    print(f"Ud mantiene una deuda de {deuda}")
                    monto_pagar= int(input("Ingrese monto a pagar: "))
                    if monto_pagar > 0 and monto_pagar<= deuda:
                        if monto_pagar<=deuda:
                            deuda= deuda-monto_pagar
                            cupo_disponible= cupo_disponible+monto_pagar
                            print(f"Ud pagó {monto_pagar}")
                            print(f"Su cupo actual es {cupo_disponible}")
                            break
                    elif monto_pagar<0:
                        print(f"Ingrese una cantidad valida")
                    elif monto_pagar > deuda:
                        print(f"No puede abonar un monto mayor a su cupo")
                except:
                    print("Debe ingresar solo numeros")
# 2.	Simulación de Compras:
# a.	El usuario puede simular realizar un número ilimitado de compras.
# b.	Para cada compra, se solicita al usuario ingresar el monto de la compra. El programa suma los montos de cada compra. 
# c.	Se verifica que el monto de la compra sea mayor o igual a cero.
# d.	Se realiza la compra y se actualiza el saldo de la tarjeta para cada iteración del bucle for.
# 3.	Salir:
# a.	Al seleccionar esta opción, el programa debe cerrarse o finalizar.
        elif op ==2:
            while True:
                try:
                    print("Comprando...")
                    print(f"Recuerde: su cupo actual es {cupo_disponible}")
                    monto_comprar= int(input("Ingrese monto a de su compra: "))
                    if monto_comprar >= 0 and monto_comprar <= cupo_disponible:
                        cupo_disponible= cupo_disponible-monto_comprar
                        deuda = deuda+monto_comprar
                        print(f"Compra realizada por {monto_comprar}")
                        print(f"Su cupo disponible es {cupo_disponible}")
                        break
                    elif monto_comprar > cupo_disponible: 
                        print(f"No puede comprar más que el cupo")
                        print(f"Su cupo actual es {cupo_disponible}")   
                        break            
                    elif monto_comprar < 0:
                        print(f"Ingrese una cantidad valida")
                except:
                    print("Debe ingresar solo numeros")
                    
        elif op==3:
            print("Saliendo")
            break
        else:
            print("Elija una opcion valida")       
    except:
        print("Debe ingresar solo numeros")

# A considerar:
# 1.	Manejo de Errores
# a.	Se utilizan bloques try y except para manejar posibles errores al in-gresar datos, validar valores no numéricos y errores   inesperados. 
# b.	Se debe programar mensajes de error específicos para guiar al usuario sobre posibles problemas.


