import random as rd

num_sec=rd.randint(1,500)
# EJERCICIO: JUEGO DE ADIVINANZA CON MENU
#
# Objetivo:
# Crear un programa con menu para jugar a adivinar un numero secreto.
#
# El menu debe mostrar:
# 1. Jugar
# 2. Ver cantidad de intentos del ultimo juego
# 3. Reiniciar juego
# 4. Salir
intentos=0
while True:
    try:
        print("Juego de adivinanzas")
        print("1. Jugar")
        print("2. Ver cantidad de intentos del ultimo juego")
        print("3. Reiniciar el juego")
        print("4. Salir")
        op=int(input("Ingresa tu opcion: "))
        if op==1:
            while True:
                print("*Menu de juego*")
                intentos=intentos+1
                adivinacion=int(input(f"*1Ingrese su intento N.{intentos}: "))
                
                if adivinacion==num_sec:
                    print(f"*Felicidades! ganaste al intento N. {intentos}")
                    break
                elif adivinacion>num_sec:
                    print("*El numero secreto es menor que tu adivinacion, intenta nuevamente")
                    continue
                elif adivinacion<num_sec:
                    print("*El numero secreto es mayor que tu adivinacion")
                    continue
        elif op==2:
            print("*Ver intentos*")
            if intentos==0:
                print("*No ha jugado todavia, no hay intentos para mostrar")
            else:
                print(f"*intentos realizados: {intentos}")
                input("*Presiona ENTER para volver al menu principal")        
                continue
        elif op==3:
            print("*Juego reiniciado!")
            intentos=0
            num_sec=rd.randind(1-500)
            continue
        elif op==4:
            print("*Ha salido del juego")
            break
        elif op<1 or op>4:
            print("*Opcion invalida, Ingrese una opcion 1-2-3-4")    
    except ValueError:
        print("*Debes ingresar solo numeros")
    
    
# Reglas:
# - El programa debe tener un numero secreto guardado en una variable.
# - Cuando el usuario juegue, debe ingresar numeros hasta adivinar.
# - El programa debe indicar si el numero secreto es mayor o menor.
# - Debes contar cuantos intentos tarda en adivinar.
# - Si el usuario aun no juega y pide ver intentos, mostrar un mensaje avisando eso.
# - La opcion reiniciar debe volver a dejar la cantidad de intentos en 0 y cambiar el numero secreto.
#
# Pistas:
# - Puedes partir con numero_secreto = 7
# - Usa una variable intentos = 0
# - Dentro de la opcion jugar, crea otro while para seguir preguntando hasta adivinar.
# - Usa try/except para validar que el usuario escriba numeros.
#
# Desafio extra:
# - Haz que el numero secreto cambie de forma aleatoria usando random.