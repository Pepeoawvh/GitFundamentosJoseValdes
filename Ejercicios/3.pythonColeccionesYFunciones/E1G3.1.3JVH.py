# Ejercicio	Completar con las sentencias de código, que permitan realizar: 
# 1.- Agregar notas a la lista creada
# 2.- Muestre por pantalla todas las notas ingresadas
# 3.- Muestra la cantidad de notas ingresadas
# 4.- Obtenga el promedio de las notas


#promedioNotas
sw = 1
listaNotas = []

print("Presione 1 para ingresar sus notas")
print("Presione cualquier tecla para salir")
op=int(input("Seleccione opción: "))

if(op == 1):
    listaNotas=[]
    while sw==1:
        try:
            
            print("----------------------------------------------------------")
            nota=int(input("Incorpore su nota, si desea salir, presione 0: ")) 
            if(nota != 0):
                listaNotas.append(nota)
                print(f"Cantidad de Notas Ingresadas: {len(listaNotas)}")
                print(f"Notas Ingresadas: {listaNotas}")
                print(f"Promedio de notas: {sum(listaNotas) / len(listaNotas):.2f}")
                
                
# AQUÍ VA EL CÓDIGO FALTANTE

            else:
                print("Adiós")
                sw=0
        except:
            print("Ingreso Erróneo")
else:
    print("Adiós")