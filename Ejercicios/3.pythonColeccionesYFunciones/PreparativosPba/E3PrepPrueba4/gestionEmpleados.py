dotacion=[]
###
def agregarEmpleado(dotacion):
    print("===== MENU DE REGISTRO DE EMPLEADO ======")
    while True:
        nombre=input("Ingrese nombre de empleado: ")
        if not validarTexto(nombre):
            print("No puede dejar el campo vacio,reintente")
            continue
        else:
            break
    while True:            
        cargo=input("Ingrese el cargo del empleado: ")
        if not validarTexto(cargo):
            print("No puede dejar el campo vacio, reintente")
            continue
        else:
            break
    while True:
        salario=int(input("Ingrese salario del empleado: "))
        if salario<0:
            print("Ingrese Numeros enteros mayores a 0")
            continue
        else:
            break
        #CUANDO ESTA todo PEDIDO se  crea el diccionario y luego se agrega a la lista = lista.append(diccionarioEnVariable)      #el diccionario se asigna a una variable quqe luego se agrega
    empleado={
        "nombre":nombre,
        "cargo":cargo,
        "salario":salario,
        "bono":False}
    dotacion.append(empleado)
    print("Empelado agregado exitosamente")
###
def buscarEmpleado(dotacion):
    while True:
        busqueda=input("Ingrese nombre de empleado: ")
        if not validarTexto(busqueda):
            print("No puede dejar el campo vacio,reintente")
            continue
        else:
            break  #para buscar en diccionario se recorre la lista en su longitud con contador para ubicar la posicion  
    for i in range(len(dotacion)): #para i en el rango del largo de la lista dotacion (recorrer la lista)
        if dotacion[i]["nombre"]==busqueda: #leer de derecha a izquierda: si busqueda es igual al [nombre] en la posicion [i] de la lista dotacion
            return i # retornar i que es el numero de posicion de la lista, despues se usa para encontrar el objeto
        return -1 # si no esta retorna este valor que es para negarlo
###
def calcularBono(dotacion):

    for empleado in dotacion:
        salario=empleado["salario"]
        if salario <= 800000:
            empleado["bono"]=True
        else:
            empleado["bono"]=False
    print("***Informacion de bonificacion actualizada correctamente")
###
def mostrarDotacion(dotacion):
    for empleado in dotacion:
        print("*********************************")
        print("nombre: ", empleado["nombre"] )
        print("cargo: ", empleado["cargo"] )
        print("salario: ", empleado["salario"] )
        if empleado["bono"] == True:
            print("Bono: Aprobado" )
        else:
            print("Bono: No rige" )
        print("*********************************")
###
def validarTexto(string):
    return len(string.strip()) > 0
### 
def mostrarMenu():
        print("======== Menu Gestion de Empleados =========")
        print("1. Agregar Empleado")
        print("2. Buscar Empleado")
        print("3. Eliminar Empleado")
        print("4. Calcular bonos")
        print("5. Mostrar empleados")
        print("6. Salir")
        print("===========================================")
###       
def pedirOp():
    while True:
        try:
            opMenu=int(input("Ingrese su opcion: "))
            return opMenu
        except ValueError:
            print("Debe ingresar digitos") 
            
    #Menu principal
while True:
    mostrarMenu()
    opMenu=pedirOp()
    if opMenu==1: #agregar libro
        agregarEmpleado(dotacion)
    elif opMenu==2:
        print("======== BUSQUEDA POR NOMBRE DE EMPLEADO======")
        pos=buscarEmpleado(dotacion)
        if pos != -1:
            print("EMPLEADO ENCONTRADO")
            print("Nombre:", dotacion[pos]["nombre"])
            print("Cargo:", dotacion[pos]["cargo"])
            print("Salario:", dotacion[pos]["salario"])
        else:
            print("No existe ese empleado")
    elif opMenu==3:
        pos=buscarEmpleado(dotacion)
        if pos != -1:
            del(dotacion[pos])
            print("Empleado y su familia desvinculados exitosamente")
        else:
            print("No existe ese empleado en esta empresa")
    elif opMenu==4:
        calcularBono(dotacion)
    elif opMenu==5:
        mostrarDotacion(dotacion)
    elif opMenu==6:
        print("Saliendo, adios")
        break
    else:
        print("Opcion invalida")