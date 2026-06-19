# sistema de gestión de inventario para una tienda de
# tecnología, donde todo el comportamiento se organice mediante funciones bien definidas. El programa debe
# incluir un menú interactivo
# validaciones de entrada
# operaciones lógicas 
# uso de funciones separadas.

# # # 1.Datos que debe manejar el sistema
# # # El sistema trabaja con una colección de productos. 
# # # Esta colección debe existir desde que el programa inicia
# # # estar disponible durante toda la ejecución. 
# # # Cada vez que se agrega un producto, se incorpora a esa colección
# # # como un nuevo elemento.
# # # Cada producto se representa como 
# # # un conjunto de campos asociados: nombre, precio, stock y un indicador de si está disponible o no. 

# # Datos a manejar:

# # El sistema se controla desde un menú 
# # cada vez que el usuario termina una acción. El
# # usuario elige una opción numérica, el programa ejecuta la tarea correspondiente y vuelve a mostrar el menú.
# # Esto se repite hasta que el usuario elige salir.

# Para implementar este comportamiento debes 
# definir dos funciones separadas: 
# - una que muestre las opciones en una pantalla (sin recibir nada ni retornar nada) 
# - otra que lea y retorne la opción elegida por el usuario (sin recibir nada, retornando el número validado). 
# Ambas funciones deben invocarse en cada vuelta del ciclo.
# A continuación, se describe qué debe ocurrir al elegir cada opción:

import funciones as fn
productos={}

while True:
    fn.mostrarMenu()
    opMenu=fn.pedirOpMenu()
    if opMenu ==1:
        fn.agregarProducto(productos)
    elif opMenu==2:
        fn.buscarProducto(productos)
    elif opMenu==3:
        fn.eliminarProducto(productos)
    elif opMenu==4:
        fn.actDispo(productos)
        print("Disponibilidad actualizada")
    elif opMenu==5:
        fn.mostrarProductos(productos)
    elif opMenu==6:
        print("Saliendo del Sistema...")
        break
    
