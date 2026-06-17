#     La empresa de juegos de azar  "Lotín", desea crea una aplicación móvil que genere sorteos rápidos dentro del mismo celular.

# Para eso, le solicita crear un algoritmo que genere una lista de números de manera aleatoria donde si usted acierta, gana. 
# Las reglas son las siguientes:
#     • Los números participantes son del 1 al 49
#     • El jugador debe elegir 7
#     • Se generarán 3 rondas de conjunto de números ganadores
#     • Si el jugador acierta a una de las 3 ronda, gana



# Programe las líneas de código faltantes

import random
 
suerte = []
print("")
print("Ingrese sus 7 números del a suerte")
for numero in range(7):
    suerte.append(int(input("Ingrese número: ")))
    print("")
    print("Usted ingresó los siguientes números: ", suerte)
for ronda in range(3):
    lista = []
    for turno in range(1,7+1) :
        flag = True
        while flag :
            aleatorio = random.randint(1,49)
            if lista.count(aleatorio) == 0 :
                lista.append(aleatorio)
                flag = False
    print("")
    print("")
    print(f"Los números sorteados en la ronda {ronda+1} fueron: ")
    lista.append(aleatorio)
    print(numero)
    print("")
    contador = 0
    for numero in suerte:
        if lista.count(numero) == 1:
            contador += 1
    
    if contador == 7 :
        print("Hoy es su día de suerte. Ha ganado ¡!!!")
        for i in range(10):
            print("Eres una ganador!!!!!!!!!!")
        break
    else:
        print("Lo siento, pero no has ganado en esta ronda")
        