series={}
metricas={}
def mostrarMenu():
    print("=========== MENU PRINCIPAL ============")
    print("1. Total reproducciones de plataforma")
    print("2. Busqueda de series por rango de vistas")
    print("3. Actualizar precio de arriendo")
    print("4. Agregar Nueva Serie")
    print("5. Eliminar Serie")
    print("6. Salir")

def menuRepPlat(metricas, series):
    if series == {}:
        print("Catalogo vacio, agregue una serie primero")
        return
    buscaPlatValido=False
    while not buscaPlatValido:
        buscaPlat=input("Ingrese nombre de plataforma: ").upper()
        buscaPlatValido=validarStrVacio(buscaPlat)
        if not buscaPlatValido:
            print("No puede dejar el campo vacio")
        elif buscaPlatValido:
            cantidadRepro=reproPorPlatform(buscaPlat,series,metricas)
            print("La cantidad de Reproducciones de ", buscaPlat,"es ", cantidadRepro)
   
def reproPorPlatform(buscaPlat,series,metricas):
    cantidadRepro=0
    for codigo, datos in series.items():
                if buscaPlat == datos[1]:
                    print("Sumando datos de plataforma....")
                    cantidadRepro += metricas[codigo][1]
    return cantidadRepro
                
def menuBusqueda(series,metricas):
    if series == {}:
        print("Catalogo vacio, agregue una serie primero")
        return
    rangoValido=False
    while not rangoValido:
        try:
            rangoBase=int(input("Ingrese base del rango de reproducciones a buscar: "))
            rangoTope=int(input("Ingrese tope del rango a buscar: "))
            rangoValido=validarRango(rangoBase,rangoTope)
            if not rangoValido:
                print("El numero base no puede ser mayor al tope")
                continue
            if rangoValido:
                listaRango=buscarPorRango(rangoBase,rangoTope,series,metricas)
                if listaRango:
                    print(f"Estas son las series con visualizaciones  entre {rangoBase} y {rangoTope}")
                    print(listaRango)
                elif not listaRango:
                    print("No existen series en ese rango de visualizacion")
        except ValueError:
            print("Debe ingresar digitos")
            continue
def validarRango(rangoBase,rangoTope):
    return  0 <= rangoBase<=rangoTope        

def buscarPorRango(rangoBase, rangoTope, series, metricas):
    listaRango=[]
    for codigo, datos in metricas.items():
        if rangoBase <= datos[1] <= rangoTope:
            listaRango.append(f"{series[codigo][0]} -- {codigo}")
    if listaRango==[]:
        return False
    listaRango.sort()
    return listaRango
# def menuActualizarPrec(metricas):                   

def menuActualizarPrecio(series,metricas):
    if series == {}:
        print("No existen series en el catologo, agregue una serie")
        return
    while True: 
        codValido=False
        codExiste=False
        while not codValido or not codExiste:
            codSerie=input("Ingrese codigo de la Serie: ").upper()
            codValido=validarCodigo(codSerie)
            codExiste=codigoExiste(codSerie,metricas)
            if not codValido or not codExiste:
                print("No puede dejar el campo vacio, o el codigo no existe, reintente")
                continue
            if codValido and codExiste:
                precioValido=False
                while not precioValido:
                    try:
                        nuevoPrecio=int(input("Ingrese nuevo precio: "))
                        precioValido=validarMayorCero(nuevoPrecio)
                        if not precioValido:
                            print("Debe ingresar un numero mayor a 0")
                            continue
                    except ValueError:
                        print("Debe ingresar solo digitos")
                        continue
                actualizarPrecio(codSerie,nuevoPrecio,metricas)
                print("Precio Actualizado Correctamente")
        validSN=False
        while not validSN:
            actualizarOtro=input("Desea actualizar otro precio? S/N")
            validSN=validarSN(actualizarOtro)
            if not validSN:
                print("Debe ingresar S o N")
                continue
            if validSN:
                if actualizarOtro=="N":
                    return
                    
    
def actualizarPrecio(codSerie,nuevoPrecio, metricas):
    if codSerie in metricas:
        metricas[codSerie][0]=nuevoPrecio
        
        
def codigoExiste(consulta,diccionario):
    return consulta in diccionario

def agregarSerie(series, metricas):
    codValido=False
    codExiste=True
    while not codValido:
        codSerie=input("Ingrese codigo de Serie: ").upper()
        codValido=validarCodigo(codSerie)
        codExiste=codigoExiste(codSerie,series)
        if not codValido:
            print("No puede dejar el campo vacio, o el codigo ya existe, reintente")
            continue
        if codExiste:
            print("El codigo ya existe, reintente")
            return False
    titValido=False
    while not titValido:
        titSerie=input("Ingrese titulo de la serie: ").upper()
        titValido=validarStrVacio(titSerie)
        if not titValido:
            print("No puede dejar el campo vacio, reintente")
            continue
    platValido=False
    while not platValido:
        platformSerie=input("Ingrese plataforma de la serie: ").upper()
        platValido=validarStrVacio(platformSerie)
        if not platValido:
            print("No puede dejar el campo vacio, reintente")
            continue
    genValido=False 
    while not genValido:
        generoSerie=input("Ingrese genero de la serie: ").upper()
        genValido=validarStrVacio(generoSerie)
        if not genValido:
            print("No puede dejar el campo vacio, reintente")
            continue
    clasifValido=False
    while not clasifValido:
        clasifSerie=input("Clasificacion, ingrese: TEEN o 18+ ").upper()
        clasifValido=validarClasif(clasifSerie)
        if not clasifValido:
            print("Debe ingresar Teen o 18+")
            continue
    originValido=False
    while not originValido:
        originSerie=input("Serie original? S/N: ").upper()
        originValido=validarSN(originSerie)
        if not originValido:
            print("Debe ingresar S o N, reintente")
            continue
        elif originSerie=="S":
            originSerie=True
        elif originSerie=="N":
            originSerie=False
    precioValido=False
    while not precioValido:
        try:
            precioSerie=int(input("Ingrese Precio de arriendo: "))
            precioValido=validarMayorCero(precioSerie)
            if not precioValido:
                print("El precio debe ser un numero entero mayor o igual a 0")
                continue
        except ValueError:
            print("Debe ingresar solo numeros, reintente")
            continue
    reproValido=False
    while not reproValido:
        try:
            reproSerie=int(input("Ingrese cantidad de reproducciones: "))
            reproValido=validarMayorCero(reproSerie)
            if not reproValido:
                print("Debe ingresar numeros mayor a 0")
                continue
        except ValueError:
            print("Error, debe ingresar solo numeros reintente")
    series[codSerie]=[titSerie, platformSerie, generoSerie, clasifSerie, originSerie]
    metricas[codSerie]=[precioSerie, reproSerie]
    return True

def menuEliminarSerie(series,metricas):
    if series=={}:
        print("Catalogo vacio, agregue una serie primero")
        return
    codValido=False
    codExiste=False
    while not codValido or not codExiste:
        codSerie=input("Ingrese codigo de serie a eliminar: ").upper()
        codValido=validarCodigo(codSerie)
        codExiste=codigoExiste(codSerie, series)
        if not codValido or not codExiste:
            print("No puede dejar el campo vacio o no codigo no existe en catalogo, reintente")
            continue
        elif codValido and codExiste:
            eliminarSerie(codSerie,series,metricas)
            print("Serie eliminada correctamente del catalogo")
        
def eliminarSerie(codSerie,series,metricas):
    del series[codSerie]
    del metricas[codSerie]
      
#validaciones
def validarCodigo(codSerie):
    if codSerie.strip()=="":
        return False
    else:
        return True    
def validarStrVacio(stringDato):
    return stringDato.strip()!=""

def validarClasif(clasifSerie):
    return clasifSerie=="TEEN" or clasifSerie=="18+"

def validarSN(validSN):
    return validSN=="S" or validSN=="N"
        
def validarMayorCero(precioSerie):
    return precioSerie >= 0    

#principal
while True:
    try:
        mostrarMenu()
        opMenu=int(input("Ingrese la opcion: "))
        if opMenu==1:
            print("==== Total reproducciones ====")
            menuRepPlat(series,metricas)
        elif opMenu==2:
            print("==== Busqueda de series ====")
            menuBusqueda(series, metricas)
        elif opMenu==3:
            print("==== Actualizar Precio ====")
            menuActualizarPrecio(series,metricas)
        elif opMenu==4:
            print("==== Agregar Serie ====")
            serieAgregada=agregarSerie(series, metricas)
            if serieAgregada:
                print("Serie agregada exitosamente")
        elif opMenu==5:
            print("==== Eliminar Serie ====")
            menuEliminarSerie(series,metricas)
        elif opMenu==6:
            print("==== Saliendo... ====")
            break
        else:
            print("Ingrese una opcion valida entre 1 y 6")
            continue
    except ValueError:
        print("Debe ingresar solo digitos")
        
        