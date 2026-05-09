# El programa debe tener un menú de opciones de donde se pueda realizar el pago del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas una vez sumadas se resten al cupo disponible. 
# Las opciones disponibles deben estar construidas de la siguiente forma:
saldo=100000
while True:

    print("1. Pago tarjeta de credito")
    print("2. Simulacion de compra")
    print("3. Salir")
    op=int(input("ingrese su opcion: "))

    if op==1:
        print("Pagando... ")
        monto_pagar= int(input("Ingrese monto a pagar: "))
        if monto_pagar>= 0:
            if monto_pagar<=saldo:
                saldo= saldo-monto_pagar
                print(f"El saldo es {saldo}")
    elif op ==2:
        print("Cmprando")
    elif op==3:
        print("Saliendo")
        break
    else:
        print("Elija una opcion valida")
# 1.	Pago de Tarjeta de Crédito:
# a.	El usuario comienza con una deuda de $100.000
# b.	El usuario puede ingresar un monto para realizar un pago en la tarje-ta de crédito.
# c.	Se debe verificar que el monto ingresado sea mayor o igual a cero.
# d.	Se debe verificar que el monto a pagar no exceda el saldo actual de la tarjeta.
# e.	Al pagar el sistema debe descontar de la deuda total
# f.	Si las verificaciones son exitosas, se realiza el pago y se actualiza el saldo de la tarjeta.
# 2.	Simulación de Compras:
# a.	El usuario puede simular realizar un número ilimitado de compras.
# b.	Para cada compra, se solicita al usuario ingresar el monto de la compra. El programa suma los montos de cada compra. 
# c.	Se verifica que el monto de la compra sea mayor o igual a cero.
# d.	Se realiza la compra y se actualiza el saldo de la tarjeta para cada iteración del bucle for.
# 3.	Salir:
# a.	Al seleccionar esta opción, el programa debe cerrarse o finalizar.

# A considerar:
# 1.	Manejo de Errores:Hey, Cortana, open. Hey, Cortana. Hey, Cortana. 
# a.	Se utilizan bloques try y except para manejar posibles errores al in-gresar datos, validar valores no numéricos y errores inesperados. 
# b.	Se debe programar mensajes de error específicos para guiar al usuario sobre posibles problemas.


# Instrucciones para el envío de la actividad

# El representante del grupo deberá comprimir los programas y enviar al docente a través de Mensajes de AVA, utilizando el siguiente formato para el nombre del ar-chivo:
# NombreApellido.RAR
