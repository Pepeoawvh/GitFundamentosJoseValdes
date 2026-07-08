items={}
mercado={}
def mostrarMenu():
    print("======= MERCADO DE PRONTERA =======")
    print("1. Stock total por tipo de item")
    print("2. Busqueda de items por rango de precio")
    print("3. Actualizar precio de item")
    print("4. Agregar Nuevo Item")
    print("5. Eliminar item")
    print("6. Salir")



def menuActualizarPrecio(items,mercado):
    if mercado=={}:
        print("No existen items en el mercado, agregue uno")
        return
    while True:
        validarCodigo=False
        codExiste=False
        while not validarCodigo or not codExiste :
            codBuscar=input("Ingrese codigo del item que quiere modificar el  precio: ").upper()
            validarCodigo=validarStrVacio(codBuscar)
            codExiste=validarCodExiste(codBuscar, items)
            if not validarCodigo or not codExiste:
                print("No puede dejar el campo vacio, o el codigo no existe")
                continue
        precioValido=False
        while not precioValido:
            try:
                nuevoPrecio=int(input("Ingrese nuevo precio del item: "))
                precioValido=validarPrecio(nuevoPrecio)
                if not precioValido:
                    print("debe ingresar precio mayor a 0")
                    continue
            except ValueError:
                print("Debe ingresar solo digitos")
        actualizarPrecio(codBuscar, nuevoPrecio, mercado)
        print("Precio actualizado correctamente")
        validSN=False
        while not validSN:
            actualizarOtro=input("Desea actualizar otro precio? S/N").upper()
            validSN=validarSN(actualizarOtro)
            if not validSN:
                print("Debe ingresar S o N")
            if validSN:
                if actualizarOtro=="N":
                    return
        
def validarSN(actualizarOtro):
    return actualizarOtro=="S" or actualizarOtro=="N"      
    
    
def actualizarPrecio(codBuscar, nuevoPrecio, mercado):
    if codBuscar in mercado:
        mercado[codBuscar][0]= nuevoPrecio

def menuStockTipo(items,mercado):
    if items=={}:
        print("No hay items en la tienda, agrege uno")
        return
    validarTipo=False
    while not validarTipo:
        buscarTipo=input("Ingrese tipo de item: ").upper()
        validarTipo=validarStrVacio(buscarTipo)
        if not validarTipo:
            print("no puede dejar el string vacio")
    totalStockTipo=stockPorTipo(buscarTipo, items, mercado)
    print(f"Hay {totalStockTipo} unidades de {buscarTipo}")

def stockPorTipo(buscarTipo,items,mercado):
    totalStockTipo=0
    for codigo, datos in items.items():
        if buscarTipo == datos[1]:
            print("Item encontrado")
            totalStockTipo += mercado[codigo][1]
    return totalStockTipo
            
def menuItemRango(items,mercado):
    if items=={}:
        print("No hay items en la tienda, agregue uno")
        return
    rangoValido=False
    while not rangoValido:
        try:
            rangoBase=int(input("Ingrese base del rango a buscar: "))
            rangoTope=int(input("Ingrese tope del rango a buscar: "))
            rangoValido=validarRango(rangoBase, rangoTope)
            if not rangoValido:
                print("Debe ingresar numeros positivos, rango base no puede ser mayor a rango Tope")
                continue
        except ValueError:
            print("Debe ingresar solo digitos")
    listaRango=buscarPorRango(rangoBase, rangoTope, items, mercado)
    if not listaRango:
        print("No hay items en este rango de precio")
    elif listaRango:
        print(f"Estos son los productos en el rango de precio {rangoBase} - {rangoTope}")
        print(listaRango)

def buscarPorRango(rangoBase, rangoTope, items, mercado):
    listaRango=[]
    for codigo,datos in mercado.items():
        if rangoBase <= datos[0] <= rangoTope and datos[1] > 0:
            listaRango.append(f"{items[codigo][0]} -- {codigo}")
    if listaRango == []:
        return False
    listaRango.sort()
    return listaRango
           
def validarRango(rangoBase, rangoTope):
    return 0<= rangoBase <= rangoTope
         
    
def agregarItem(items, mercado):
    validarCodigo=False
    codExiste=True
    while not validarCodigo or codExiste:
        codItem=input("Ingrese Codigo de item: ").upper()
        validarCodigo=validarStrVacio(codItem)
        codExiste=validarCodExiste(codItem,items)
        if not validarCodigo:
            print("No puede dejar el campo vacio")
            continue
        elif codExiste:
            print("El ya existe un item con ese codigo en el mercado, reintente")
            continue
    validarNombre=False
    while not validarNombre:
        nombreItem=input("Ingrese nombre del item: ").upper()
        validarNombre=validarStrVacio(nombreItem)
        if not validarNombre:
            print("No puede dejar el campo vacio")
            continue
    validarTipo=False
    while not validarTipo:
        tipoItem=input("Ingrese tipo de item: ").upper()
        validarTipo=validarStrVacio(tipoItem)
        if not validarTipo:
            print("No puede dejar el cambio vacio")
            continue
    validarJob=False
    while not validarJob:
        jobReqItem=input("Ingrese Job requerido para usar el item: ").upper()
        validarJob=validarStrVacio(jobReqItem)
        if not validarJob:
            print("No puede dejar el campo vacio")
    validarRareza=False
    while not validarRareza:
        rarezaItem=input("Ingrese categoria de rareza del item NORMAL-RARO-EPICO-LEGENDARIO: ").upper()
        validarRareza=validRareza(rarezaItem)
        if not validarRareza:
            print("Debe ingresar la categoria exacta")
            continue
    validarComerciable=False
    while not validarComerciable:
        comerciableItem=input("Item comercialbe? S/N: ").upper()    
        validarComerciable=validarItemComerciable(comerciableItem)
        if not validarComerciable:
            print("Debe ingresar S or N")
        if comerciableItem == "S":
            comerciableItem= True
        if comerciableItem == "N":
            comerciableItem= False
    validPrecio=False
    while not validPrecio:
        try:
            precioItem=int(input("Ingrese precio del item: "))
            validPrecio=validarPrecio(precioItem)
            if not validPrecio:
                print("Debe ingresar numero mayor a 0")
                continue
        except ValueError:
            print("Debe ingresar solo digitos enteros")
            continue
    validStock=False
    while not validStock:
        try:
            stockItem=int(input("Ingrese stock del item: "))
            validStock=validarStock(stockItem)
            if not validStock:
                print("Debe ingresar numero mayor o igual a 0")
                continue       
        except ValueError:
            print("Debe ingresar solo digitos")
            continue
    items[codItem]=[nombreItem, tipoItem, jobReqItem, rarezaItem, comerciableItem]
    mercado[codItem]=[precioItem, stockItem]
    print("Item agregado exitosamente ")
    
def menuEliminarItem(items,mercado):
    if items=={}:
        print("No hay productos en el mercado, agregue uno")
        return
    codValido=False
    codExiste=False
    while not codValido or not codExiste:
        codEliminar=input("Ingrese codigo de item a eliminar: ").upper()
        codValido=validarStrVacio(codEliminar)
        codExiste=validarCodExiste(codEliminar,items)
        if not codValido or not codExiste:
            print("No puede dejar el campo vacio, o el codigo no existe en mercado")
            continue
    eliminarItem(codEliminar,items,mercado)
    print("Item eliminado correctamente")
    
def eliminarItem(codEliminar,items,mercado):
    if codEliminar in items:
        del items[codEliminar]
        del mercado[codEliminar]                
    
def validarPrecio(precioItem):
    return precioItem > 0

def validarStock(stockItem):
    return stockItem >= 0    
    
def validarItemComerciable(comerciableItem):
    return comerciableItem == "N" or comerciableItem == "S"
        
def validRareza(rarezaItem):
    if rarezaItem == "NORMAL" or rarezaItem == "RARO" or rarezaItem == "EPICO" or rarezaItem == "LEGENDARIO":
        return True
    else:
        return False    
        
def validarStrVacio(string):
    return string.strip() != ""
     
def validarCodExiste(codItem,items):
    return codItem in items
#PRINCIPAL
while True:
    try:
        mostrarMenu()
        opMenu=int(input("Ingrese su opcion: "))
        if opMenu==1:
            print("===== STOCK POR TIPO DE ITEM =====")
            menuStockTipo(items,mercado)
        elif opMenu==2:
            print("===== BUSQUEDA POR RANGO =====")
            menuItemRango(items,mercado)
        elif opMenu==3:
            print("===== ACTUALIZAR PRECIO =====")
            menuActualizarPrecio(items, mercado)
        elif opMenu==4:
            print("===== AGREGAR ITEM =====")
            agregarItem(items,mercado)
        elif opMenu==5:
            print("===== ELIMINAR ITEM =====")
            menuEliminarItem(items,mercado)
        elif opMenu==6:
            print("Saliendo....")
            break
        else:
            print("Debe ingresar una opcion valida entre 1 y 6")
    except ValueError:
        print("Debe ingresar solo digitos, del 1 al 6")