arreglos={}
bodega={}

def mostrarMenu():
    print("1. Unidades por tipo de arreglo")
    print("2. Busqueda de arreglos por rango de precio")
    print("3. Actualizar Precio de Arreglo")
    print("4. Agregar arreglo")
    print("5. Eliminar Arreglo")
    print("6. Salir")
    
def opciontipoBuscado(arreglos,bodega):
    validarBusqueda=False
    while not validarBusqueda: 
        tipoBuscado=input("Ingrese tipo de arreglo a buscar: ")
        validarBusqueda=validarTexto(tipoBuscado)
        if validarBusqueda:
            unidadesTipo(tipoBuscado,arreglos,bodega)
        elif not validarBusqueda:
            print("no puede dejar el campo vacio")
    return tipoBuscado

def unidadesTipo(tipoBuscado,arreglos,bodega):
    cantidadArreglos=0
    tipoBuscado= tipoBuscado.strip().upper()
    for codigo,datos in arreglos.items():
        if tipoBuscado==datos[1]:
            print("Encontrado")
            cantidadArreglos += bodega[codigo][1]
            
            
    print("La cantidad de  arreglos diponibles para el tipo", tipoBuscado,"es", cantidadArreglos )

def opcionBusquedaPrecio(arreglos,bodega):
    while True:
        try:
            rangoMin=int(input("Ingrese base del rango a buscar: "))
            rangoMax=int(input("Ingrese tope del rango a buscar: "))
            if rangoMin > rangoMax:
                print("rango base no puede ser mayor ni igual al rango tope reintente")
                continue
            elif rangoMin < 0 or rangoMax < 0:
                print(" Los rangos no peuden ser menores a 0")
                continue     
            else:
                break
        except ValueError:
            print("Debe ingresar solo digitos")
    recorrerPorRango(rangoMin, rangoMax, arreglos, bodega)
            
def recorrerPorRango(rangoMin, rangoMax, arreglos, bodega):
    listaRango=[]
    for codigo,datos in bodega.items():
        if  rangoMin <= datos[0] <= rangoMax and datos[1] != 0:
            codigoLista=codigo
            nombreLista=arreglos[codigo][0]
            listaRango.append(f"{nombreLista}--{codigoLista}")
    if listaRango==[]:
        print("No hay Arreglos en ese rango de precio")
        return
    listaRango.sort()
    print(listaRango)                    
        
def agregarArreglo(arreglos,bodega):
    validarCod=False
    codigoExistente=True
    while not validarCod or codigoExistente:
        codArreglo=input("Ingrese codigo de Arreglo: ").upper()
        validarCod=validarCodigo(codArreglo)
        codigoExistente=buscarCodigo(codArreglo,bodega)
        print(validarCod)
        if not validarCod or codigoExistente:
            print("Error: el nombre no puede estar vacio ni existir previamente")
    validarNom=False       
    while not validarNom:
        nomArreglo=input("Ingrese Nombre de arreglo: ").upper()    
        validarNom=validarTexto(nomArreglo)
        print(validarNom)
        if not validarNom:
            print("El nombre no puede estar vacio, ni ser un espacio")
    validarTipo=False
    while not validarTipo:
        tipoArreglo=input("Ingrese tipo de arreglo: ").upper()
        validarTipo=validarTexto(tipoArreglo)
        print(validarTipo)
        if not validarTipo:
            print("El tipo no puede estar vacio, ni ser un espacio")
    validarColor=False
    while not validarColor:
        colorArreglo=input("Ingrese color de arreglo: ").upper()
        validarColor=validarTexto(colorArreglo)
        print(validarColor)
        if not validarColor:
            print("El color no puede estar vacio, ni ser un espacio")
    validarTam=False
    while not validarTam:
        tamanoArreglo=input("Ingrese Tamano de Arreglo: ").upper()
        validarTam=validarTamano(tamanoArreglo)
        print(validarTam)
        if not validarTam:
            print("El tamano debe ser S, M o L")
    validarTarj=False
    while not validarTarj:
        tarjeta=input("Incluye tarjeta? S/N: ").upper()
        validarTarj=validarTarjeta(tarjeta)
        if tarjeta == "N":
            tarjeta=False
        elif tarjeta == "S":
            tarjeta=True
        if not validarTarj:
            print("Debe ingreser S o N")
    validarTemp=False
    while not validarTemp:
        temporadaArreglo= input("Indique temporada de disponibilidad estacion/todo el ano: ").upper()
        validarTemp=validarTexto(temporadaArreglo)
        if not validarTemp:
            print("La temporada no puede estar vacia, reingrese")
    validarPrec=False
    while not validarPrec:
        try:
            precioArreglo=int(input("Ingrese Precio: "))
            validarPrec=validarPrecio(precioArreglo)
            if not validarPrec:
                print("Debe ingresar num enteros mayor a 0")
        except ValueError:
            print("Debe ingresar solo digitos, enteros")
    validarUnid=False
    while not validarUnid:
        try:
            unidadArreglo=int(input("Ingrese Stock: "))
            validarUnid=validarUnidad(unidadArreglo)
            if not validarUnid:
                print("Debe ingresar num enteros mayor o igual 0")
        except ValueError:
            print("Debe ingresar solo digitos, enteros")
    arreglos[codArreglo]=[nomArreglo, tipoArreglo, colorArreglo, tamanoArreglo]
    bodega[codArreglo]=[precioArreglo, unidadArreglo]
    print("Arreglo agregado exitosamente")       

def opcionActualizarPrecio(bodega):
    validarBusqueda=False
    while not validarBusqueda:
        codigoBuscar=input("Ingrese Codigo de arreglo a buscar: ").upper()
        validarBusqueda=validarCodigo(codigoBuscar)
        if validarBusqueda:
            codigoExiste=buscarCodigo(codigoBuscar, bodega)
            if codigoExiste:
                actualizacionPrecio=actualizarPrecio(codigoBuscar,bodega)
                if actualizacionPrecio:
                    print("El Precio se actualizo correctamente")
                    return
                elif not actualizacionPrecio:
                    print("El precio no fue actualizado")
                    return
                
            if not codigoExiste:
                print("El codigo no existe en el catalogo")
                return

def actualizarPrecio(codigoBuscar, bodega):
    validarPrec=False
    while not validarPrec:
        try:
            actPrecio=int(input("Ingrese precio a reemplazar: "))
            validarPrec=validarPrecio(actPrecio)
            if not validarPrec:
                print("Debe ingresar num enteros mayores a 0")
        except ValueError:
            print("Debe ingresar solo digitos")
    while True:
        confirmPrecio=input("Segun que desea cambiar el precio? s/n: ").upper()
        if confirmPrecio=="S":
            bodega[codigoBuscar][0]=actPrecio
            return True
        elif confirmPrecio=="N":
            return False
        elif confirmPrecio!= "N" and confirmPrecio!="S":
            print("Debe ingresar respuesta 'N' o 'S'")
            continue
            
def buscarCodigo(codigoBuscar, lista):
    return codigoBuscar in lista 

def opcionEliminarPrecio(arreglos,bodega):
    validarBusqueda=False
    while not validarBusqueda:
        codigoEliminar=input("Ingrese Codigo de arreglo a buscar: ").upper()
        validarBusqueda=validarCodigo(codigoEliminar)
        if validarBusqueda:
            codigoExiste=buscarCodigo(codigoEliminar,arreglos)
            if codigoExiste:
                eliminarCod=eliminarBusqueda(codigoEliminar,arreglos,bodega)
                if eliminarCod:
                    print("Codigo eliminado correctamente")
            elif not codigoExiste:
                print("El codigo ingresado no existe en catalogo, reintente")
                return
def eliminarBusqueda(codigoEliminar,arreglos,bodega):
    del arreglos[codigoEliminar]
    del bodega[codigoEliminar]
    return True
    

    
# validaciones
def validarCodigo(codArreglo):
    return codArreglo.strip() != "" 

def validarTexto(texto):
    return texto.strip() != ""

def validarTamano(tamano):
    return tamano=="L" or tamano=="M" or tamano=="L"

def validarTarjeta(tarjeta):
    return tarjeta == "S" or tarjeta == "N"

def validarPrecio(precio):
    return 0 < precio

def validarUnidad(unidad):
    return 0 <= unidad

##########################

                
# principal:

while True:
    mostrarMenu()
    try:
        opMenu=int(input("Ingrese su opcion: "))
        if opMenu==1:
            print("=== Unidades por tipo ===")
            opciontipoBuscado(arreglos,bodega)
        elif opMenu==2:
            print("=== Busqueda de arreglos por precio ===")
            opcionBusquedaPrecio(arreglos,bodega)
        elif opMenu==3:
            print("=== Actualizar precio de arreglo ===")
            opcionActualizarPrecio(bodega)
        elif opMenu==4:
            print("=== Agregar arreglo ===")
            agregarArreglo(arreglos,bodega)
        elif opMenu==5:
            print("=== Eliminar Arreglo ===")
            opcionEliminarPrecio(arreglos, bodega)
        elif opMenu==6:
            print("Saliendo")
            break
    except ValueError:
        print("*Error: Debe ingresar solo digitos")