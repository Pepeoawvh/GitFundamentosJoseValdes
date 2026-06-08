

productos={} #se inicializa la biblioteca
producto="" # se inicializa variable producto
stock=0 #inicializa variable stock valor 0
precio=0 #inicializa variable precio valor 0

def agregar_producto(productos):
    
    #asigna valor string a variable "producto" segun input
    while True:
        print("-----Menu de Agregar Producto----")
        producto=input("Ingrese nombre del producto: ")
        if producto == "":
            print("No puede dejar el campo vacio, reintente")
            continue
        elif producto in productos:
            print("Producto ya existe, reintente")
            continue
    #asigna valor numerico entero a variable "producto" sstock segun input
        else:
            stock=int(input("Ingrese stock del producto: "))
            if stock < 0 or stock == "":
                print("Debe ingresar una cantidad valida, reingrese")
                continue
            else:
                #asigna valor numerico entero a variable "precio" stock segun input
                precio=int(input("Ingrese precio del producto: "))
                if precio <= 0 or precio == "":
                    print("Ingrese un precio valido, reingrese")
                else:
                     #EN DICCIONARIO "productos" agrega variable "producto" como clave, y como valor, una lista donde en la p.0 se agrega la variable "stock", y en p.1 la variable "precio"
                    productos[producto]=[stock,precio]
                    print(f" {producto} agregado")  
                    break
                    # se imprime el diccionario productos
    
def mostrar_productos(productos):
    print("----Mostrar Productos----")   
    if not productos:
        print("El inventario esta vacio, agregue productos primero")
    else:
        print(f"Estos son los productos del inventario {productos}")

def buscar_producto(productos):
    if not productos:
        print("El inventario esta vacio, agregue productos primero")
    elif productos: 
        busqueda=input("Ingrese nombre de producto a buscar: ").strip().lower()
        if busqueda in productos:
            print(f"Producto encontrado! {busqueda} Stock: {productos[busqueda][0]}, Precio: {productos[busqueda][1]}")
        else:
            print("No se encontro el producto, intente nuevamente")
    
def producto_mas_caro(productos):
    print("----Producto mas caro----")
    if not productos:
        print("El inventario esta vacio, agregue productos primero")
    else:
        precioMax=0
        productoMax=""
        for producto in productos:
            precio= productos[producto][1]
            if precio > precioMax:
                precioMax=precio
                productoMax=producto
        #inicializar un loop que recorre los indices de la biblioteca
        
        print(f"Nuestro producto mas caro es {productoMax} y su valor es {precioMax}")