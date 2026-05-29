#CajeroAutomático
sw = 1
while sw==1:
    print("1. Ver mi Saldo")
    print("2. Retirar Dinero")
    print("3. Salir")
    op=int(input("Seleccione una opción: "))
    try:
        if(op > 0 and op < 4):
            if op == 1:
                print("Tiene un saldo de $500000")
                continua = int(input("presione 1) para volver atrás, presione 2) para salir "))
                if continua==2:
                    print("Cierre de sesión exitoso, adiós")
                    sw=0
            if op == 2:
                print("Transferencia realizada")
                continua = int(input("presione 1) para volver atrás, presione 2) para salir "))
                if continua==2:
                    print("Cierre de sesión exitoso, adiós")
                    sw=0
            if op == 3:
                print("Cierre de sesión exitoso, adiós")
                sw=0
        else: 
            print("Selección fuera de rango")
    except:
        print("Ingreso Erróneo")