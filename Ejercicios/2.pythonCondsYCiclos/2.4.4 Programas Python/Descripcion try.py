try:
    # Código que podría generar una excepción
    # Dentro de este bloque de código, debes colocar 
    # lo que quieres validar por medio de una 
    # excepción, ejemplo, operaciones matemáticas, 
    # Set de variables, etc....
    resultado = 10/ 0
except ZeroDivisionError as nombre_de_excepcion:
    # Código para manejar la excepción
    print(f"Se produjo una excepción: {nombre_de_excepcion}")
else:
    # Código a ejecutar si no se produjo ninguna excepción
    print("No se produjo ninguna excepción")
finally:
    # Código a ejecutar siempre, independientemente de si se produjo una excepción o no
    print("Este bloque se ejecuta siempre")