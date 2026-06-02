#listaSuper
sw = 1
print("Presione 1 para ingresar los productos del súper")
print("Presione cualquier tecla para salir")
op=int(input("Seleccione opción "))
if(op == 1):
    listaSuper=[]
    valorSuper=[]
    while sw==1:
        try:
            print("----------------------------------------------------------")
            producto=input("Incorpore su producto, para salir, presione 0: ")
            if(producto != "0"):
                listaSuper.append(producto)
                valorProducto=int(input(f"Ingrese el valor de {producto}: "))
                valorSuper.append(valorProducto)                        
            else:
                print("Adiós")
                sw=0
        
        except:
            print("Ingreso Erróneo")
            
    print("------------DETALLE BOLETA---------------")
    print(f"Los productos comprados fueron {listaSuper}")
    print(f"Compraste {len(listaSuper)} productos")
    print(f"El valor total es: {sum(valorSuper)}")        
else:
    print("Adiós")
# Compltar con las sentencias de código, que permitan realizar: 
# 1.- Agregar productos a la lista del súper
# 2.- Muestre mensaje indicado “Incorpore el valor del {producto}:”
# 3.- Agregue el valor del producto a la lista “valorSuper”
# 4.- Muestre mensaje indicando “----DETALLE BOLETA-----”
# 5.- Muestre mensaje indicando los productos comprados
# 6.- Muestre mensaje indicando la cantidad de productos comprados
# 7.- Muestre mensaje indicando la suma total de todos los productos