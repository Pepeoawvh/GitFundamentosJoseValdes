# Deuda tarjeta de crédito
deuda_tarjeta = 100000

while True:
    print("\nMenú de Opciones:")
    print("1. Pagar Tarjeta de Crédito")
    print("2. Realizar Compras")
    print("3. Salir")

    opcion = input("Seleccione una opción (1-3): ")

    try:
        opcion = int(opcion)
        if opcion == 1:
            try:
                monto_pago = float(input("Ingrese el monto a pagar: $"))
                if monto_pago < 0:
                    raise ValueError("El monto debe ser mayor o igual a cero.")
                
                if monto_pago > deuda_tarjeta:
                    print("El monto a pagar es mayor que el saldo actual.")
                else:
                    deuda_tarjeta -= monto_pago
                    print(f"Has realizado un pago de ${monto_pago}. Nuevo saldo: ${deuda_tarjeta}")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")
        elif opcion == 2:
            try:
                num_compras = int(input("Ingrese el número de compras que desea simular: "))
                for _ in range(num_compras):
                    monto_compra = float(input("Ingrese el monto de la compra: $"))
                    deuda_tarjeta -= monto_compra
                    print(f"Has realizado una compra de ${monto_compra}. Nuevo saldo: ${deuda_tarjeta}")
            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")
        elif opcion == 3:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2, o 3.")
    except ValueError:
        print("Error: Por favor, ingrese un número entero válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")
