def mostrarMenu():
    print("--MENU--")
    print("1. Agregar Libro")
    print("2. Buscar Libro")
    print("3. Eliminar Libro")
    print("4. Registrar Prestamo")
    print("5. Mostrar Libros")
    print("6. Salir")
    
    
def leerOpcion():
    while True:
        try:
            opcion= int(input("Ingrese su opcion: "))
            return opcion
        except ValueError:
            print("Error, debe ingresar numero!")
    
 ########## AGREGAR LIBRO ##########################   
def agregarLibro(libros):
    titulo= input("Ingrese titulo del libro: ")
    if not validarTexto(titulo):
        print("error")
        return    
    autor= input("Ingrese el Autor del libro: ")
    if not validarTexto(autor):
        print("error")
        return
    while True:
        try:
            anio=int(input("ano de la edicion: "))
            if not validarAnio(anio):
                print("Error, el anio debe estar entre 1000 y 2025")
            else:
                break
        except ValueError:
            print("***Error ingrese solo numeros")
    libro={"titulo":titulo,
           "autor":autor,
           "anio":anio,
           "prestado":False}
    libros.append(libro)
    print("Libro registrado exitosamente")
##################################################
##################### BUSCAR LIBRO ###############
def buscarLibro(libros):
    while True:
        titulo=input("Ingrese el titulo del libro")
        if not validarTexto(titulo):
            print("error, campo vacio, reintente")
            continue
        else:
            for i in range (len(libros)):
                if libros[i]["titulo"]==titulo:
                    return i
            return -1
################################################## 
##################### ELIMINAR LIBRO #############
def eliminarLibro(libros,pos):
        print(f"Libro {libros[pos]["titulo"]} eliminado correctamente")
        del(libros[pos])
################################################## 
############ REGISTRO PRESTAMO ###################
def registrarPrestamo(libros):
    for libro in libros:
        if libro["anio"] >2000:
            libro["prestado"] = "Disponible para prestamo"
        else:
            libro["prestado"] = "Solo consulta en sala"
    return 1

##################################################
################# MOSTRAR LIBROs #################
def mostrarLibros(libros):
    print("LISTA DE TODOS LOS LIBROS")
    for libro in libros:
        print("*********************************")
        print("Titulo: ", libro["titulo"] )
        print("Autor: ", libro["autor"] )
        print("Anio: ", libro["anio"] )
        print("Anio: ", libro["prestado"] )
        print("*********************************")
    return
##################################################
############ VALIDAR ANIO ########################
def validarAnio(valor):
    return 1000 <= valor <= 2025 #forma corta de if valor mayor igual mil and valor emnor igual 2025
##################################################
############# VALIDAR TEXTO ######################
def validarTexto(valor):
    return len(valor.strip())>0 #retorna True si ocure
##################################################

# Principal
libros=[]   
while True: 
    mostrarMenu()
    op=leerOpcion()
    
    if op==1:
        agregarLibro(libros) #agregar libro
    elif op==2:
        pos= buscarLibro(libros)
        if pos != -1:
            print("Titulo: ", libros[pos]["titulo"] )
            print("Autor: ", libros[pos]["autor"] )
            print("Anio: ", libros[pos]["anio"] )
    elif op==3:
        pos= buscarLibro(libros)
        if pos != -1:
            eliminarLibro(libros,pos)
    elif op==4:
        actPrestamo=registrarPrestamo(libros)
        if actPrestamo==1:
            print("Estados de prestamo actualizado")                    
    elif op==5:
        registrarPrestamo(libros)
        mostrarLibros(libros)
    elif op==6:
        print("saliendo")
        break
    else:
        print("Opcion no valida")