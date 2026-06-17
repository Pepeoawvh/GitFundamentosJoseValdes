def mostrarMenu():
    print("========== MENU PRINCIPAL ==========")
    print("1. Agregar Producto")
    print("2. Buscar Producto")
    print("3. Eliminar Producto")
    print("4. Actualizar Disponibilidad")
    print("5. Mostrar Productos")
    print("6. Salir")

def pedirOpMenu():
    while True:
        try:
            opMenu=int(input("Ingrese su opcion: "))
            if opMenu <= 6 and opMenu >= 1:
                return opMenu
            else:
                print("*ERROR: Debe ingresar una opcion valida")
        except ValueError:
                print("ERROR: Debe ingresar un numero")
# Opción 1 - Agregar producto:
# El sistema solicita al usuario 
# el nombre (no puede estar vacío ni ser solo espacios en blanco.

# el precio (El precio debe ser un número decimal mayor que cero.
# el stock del producto. ( El stock debe ser un número entero mayor o igual a cero.
# Antes de guardar el registro, verifica
# Si algún dato no cumple la condición, el sistema informa al usuario y no registra el producto. 
# Solo cuando todos los datos son válidos se crea el diccionario y se agrega a la lista.
# Para implementar esta opción debes definir una función que reciba la lista como parámetro. Dentro de ella se
# solicitan los datos al usuario y se llama a una función de validación distinta para cada campo. Los mensajes de
# error se muestran en esta función, no dentro de las validaciones.
productos={}
def agregarProducto(productos):
    print("=======AGREGAR PRODUCTO=======")
    while True:
        producto=input("Ingrese nombre de producto: ")
        if producto.strip()=="":
            print("*ERROR no puede dejar el nombre vacio reintente")
            continue
        elif producto in productos:
            print("El producto ya se encuentra en stock")
            continue
        elif producto.isnumeric():
            print("El nombre no puede contener unicamente digitos")
            continue
        else:
            print("Nombre Ingresado Correctamente")
            break        
    while True:
        try:
            precio=float(input("Ingrese el precio del producto: "))
            if precio <= 0:
                print("El precio debe ser mayor a 0")
            else:
                print("Precio ingresado correctamente")
            break
        except ValueError:
            print("*ERROR: Debe ingresar un numero")
    while True:
        try:
            stock=int(input("Ingrese el Stock del producto: "))
            if stock < 0:
                print("No puede ingresar stock negativo")
            else:
                print("Stock Ingresado correctamente")
                break
        except ValueError:
            print("*ERROR: Debe ingresar numeros")
    productos[producto]={"precio":precio,"stock":stock}
    print("Producto ingresado correctamente")
    return productos

# Opción 2 - Buscar producto:
# El sistema solicita un nombre al usuario y recorre la lista buscando un registro cuyo campo nombre coincida
# exactamente con el ingresado. Si lo encuentra, muestra la posición en la que está y sus datos. Si no existe
# ningún registro con ese nombre, informa al usuario.
# Para implementar esta opción debes definir una función que reciba la -lista y el nombre a buscar como
# parámetros. La función recorre la lista y retorna la posición del registro encontrado, o -1 si no existe. Es el
# programa principal quien recibe ese valor y decide qué hacer con él: si la posición es válida, muestra los datos
# del producto en esa posición; si es -1, muestra el mensaje de no encontrado.
    
def buscarProducto(productos):
    while True:
        print("======= BUSQUEDA DE PRODUCTO =====")
        busqueda=input("Ingrese nombre del producto a buscar: ")
        if busqueda in productos:
            print("Producto encontrado")
            print("Producto: ", busqueda)
            print("Precio: ", productos[busqueda]["precio"])
            print("Stock: ", productos[busqueda]["stock"])
            break
        elif busqueda.isnumeric():
            print("Los productos no tienen nombres puramente numericos, reintete")
            continue
        else:
            print("No existe el producto en nuestro catalogo")
            continue
# Opción 3 - Eliminar producto:
# El sistema solicita el nombre del producto que se desea eliminar. Para localizarlo, llama a la función de búsqueda
# definida en la opción anterior, pasándole la lista y el nombre ingresado. Si la función retorna una posición válida,
# el sistema elimina el registro en esa posición. Si retorna -1, informa al usuario con el siguiente mensaje:

def eliminarProducto(productos):
    while True:
        print("======= ELIMINAR PRODUCTO =====")
        eliminar=input("Ingrese nombre del producto a buscar: ")
        if eliminar in productos:
            print(f"Producto {eliminar} Eliminado correctamente")
            del productos[eliminar]
            break
        elif eliminar.isnumeric():
            print("Los productos no tienen nombres puramente numericos, reintete")
            continue
        else:
            print("No existe el producto en nuestro catalogo")
            continue
# Opción 4 - Actualizar disponibilidad:
# El sistema recorre la lista completa de productos y actualiza el campo "disponible" de cada registro según su
# stock: si el stock es mayor que cero, el campo pasa a True; si es igual a cero, queda en False. Esta operación
# afecta a todos los registros de la lista sin excepción.
# Para implementar esta opción debes definir una función que reciba la lista como parámetro y aplique esa regla a
# cada elemento.

def actDispo(productos):
    for producto in productos:
        if productos[producto]["stock"] > 0:
            productos[producto]["disponible"] = True
        else:
            productos[producto]["disponible"] = False

# Opción 5 - Mostrar productos:
# El sistema primero actualiza la disponibilidad de todos los productos haciendo el llamado a la función anterior,
# luego recorre la lista mostrando los datos de cada producto. El formato de salida es el siguiente:
# === LISTA DE PRODUCTOS ===
# Nombre: Mouse Inalámbrico
# Precio: $15990
# Stock: 5
# Estado: DISPONIBLE
# *******************************************
# Nombre: Cable HDMI
# Precio: $8990
# Stock: 0
# Estado: SIN STOCK
# *******************************************

def mostrarProductos(productos):
    print("===LISTA DE PRODUCTOS===")
    for producto in productos:
        print(f"Nombre: {producto}")
        print(f"Precio: {productos[producto]["precio"]}")
        print(f"Precio: {productos[producto]["stock"]}")
        disponible=productos[producto]["disponible"]
        if disponible:
            print(f"Estado: DISPONIBLE")
        else:
            print("SIN STOCK")
        print(f"********************************************")