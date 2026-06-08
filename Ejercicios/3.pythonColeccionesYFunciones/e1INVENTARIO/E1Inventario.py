import funciones as fn
productos={}
# Ejercicio 1 - Inventario de Productos
# Una tienda necesita un programa en Python para administrar su inventario de productos. La informacion
# debe almacenarse en un diccionario.
# Estructura sugerida
# productos = {
# "Mouse": [10, 15000],
# "Teclado": [5, 25000],
# "Monitor": [3, 180000]
# }
# En esta estructura, la clave corresponde al nombre del producto y el valor es una lista donde la posicion 0
# representa el stock y la posicion 1 representa el precio.

while True:
    try:
        print("-------MENU DE TIENDA ELECTRONIK------")
        print("1. Agregar producto")
        print("2. Mostrar productos")
        print("3. Buscar productos")
        print("4. producto mas caro")
        print("5. Salir")
        opMenu=int(input("Ingrese su opcion:"))
        if opMenu <=0 or opMenu >5:
            print("ingrese una opcion valida")
            continue
        elif opMenu == 1:
            #se ejecuta  la funcion y se entrega la biblioteca "productos" como parametro porque esta se inicializa fuera del scope (para que sepa de donde debe sacarla)
            fn.agregar_producto(productos)
        elif opMenu == 2:
            fn.mostrar_productos(productos)
        elif opMenu == 3:
            print("----Buscar Productos----")
            fn.buscar_producto(productos)
        elif opMenu==4:
            fn.producto_mas_caro(productos)
        elif opMenu==5:
            print("Saliendo del menu")
            break  
    except ValueError:
        print("Debe ingresar una Debe ingresar numeros")


# Requerimientos
# •
#  Agregar productos solicitando nombre, stock y precio
#  Mostrar el producto con mayor precio.
# •
#  Usar funciones para cada opcion del menu.
# •
#  Validar todos los datos ingresados por el usuario.
# Validaciones obligatorias
# •
#  El nombre del producto no puede estar vacio.
# •
#  No se debe permitir agregar un producto repetido.
# •
#  El stock debe ser un numero entero mayor o igual a 0.
# •
#  El precio debe ser un numero mayor que 0.
# •
#  La opcion del menu debe estar entre 1 y 5.
# •
#  Si no existen productos registrados, las opciones mostrar, buscar y producto mas caro deben indicarlo
# correctamente.
# Funciones obligatorias
# defdefdefdefagregar_producto(productos):
# mostrar_productos(productos):
# buscar_producto(productos):
# producto_mas_caro(productos)