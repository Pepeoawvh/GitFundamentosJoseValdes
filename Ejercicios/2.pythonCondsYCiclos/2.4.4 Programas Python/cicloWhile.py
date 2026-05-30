# ============================================================
#  TEORÍA: CICLO while — GUÍA DE ENSEÑANZA
# ============================================================
#
#  ¿Qué es while?
#  ─────────────
#  Es un ciclo que repite un bloque de código MIENTRAS
#  una condición sea verdadera.
#
#  Estructura básica:
#
#      while <condicion>:
#          # código que se repite
#          # algo debe cambiar para que la condición deje de ser True
#
#  La condición se evalúa ANTES de cada vuelta.
#  Si desde el inicio es False, el bloque nunca se ejecuta.
#
# ============================================================
#  TIPOS DE USO DEL while
# ============================================================
#
#  ① while con CONDICIÓN CONOCIDA (contador o límite)
#  ─────────────────────────────────────────────────
#  Se usa cuando sabes cuántas veces quieres repetir, o cuando
#  tienes un valor límite con el que comparar.
#
#  Ejemplo:
#      numero = 1
#      while numero <= 5:
#          print(numero)
#          numero += 1       ← ¡IMPORTANTE! sin esto, ciclo infinito
#
#  ✅ Pros:
#     - Fácil de leer, la condición de salida es visible
#     - Control claro sobre cuándo para
#  ❌ Contras:
#     - Si olvidas modificar la variable, el programa se congela
#     - Menos flexible cuando no sabes el total de repeticiones
#
# ─────────────────────────────────────────────────────────────
#  ② while True (bucle infinito con break)
#  ─────────────────────────────────────────────────────────────
#  Se usa cuando NO sabes de antemano cuántas veces se repetirá.
#  El ciclo corre para siempre hasta que tú lo detengas con break.
#
#  Ejemplo:
#      while True:
#          respuesta = input("¿Continuar? (s/n): ")
#          if respuesta == "n":
#              break         ← aquí se sale del ciclo
#
#  ✅ Pros:
#     - Útil para menús, validaciones, juegos, entrada de datos
#     - No necesitas saber cuántas repeticiones habrá
#  ❌ Contras:
#     - Si olvidas el break, el programa se congela para siempre
#     - Puede ser menos legible si la lógica de salida es compleja
#
# ─────────────────────────────────────────────────────────────
#  ③ COMPARACIÓN RÁPIDA
#  ─────────────────────────────────────────────────────────────
#
#  | Situación                              | Usa             |
#  |----------------------------------------|-----------------|
#  | Sé cuántas veces repetir               | while n <= total|
#  | No sé cuántas veces, el usuario decide | while True+break|
#  | Validar que el usuario ingrese bien    | while True+break|
#  | Recorrer una lista con índice          | while i < len() |
#
# ─────────────────────────────────────────────────────────────
#  ④ PALABRAS CLAVE dentro del while
#  ─────────────────────────────────────────────────────────────
#  break    → sale del ciclo inmediatamente
#  continue → salta el resto del bloque y vuelve a la condición
#  else     → bloque que corre UNA VEZ cuando el while termina
#             de forma normal (sin break)
#
# ─────────────────────────────────────────────────────────────
#  ESTE PROGRAMA usa: while con condición (tipo ①)
#  El ciclo recorre cada bulto del 1 hasta cantidadBultos.
#  nroBulto actúa como contador y se incrementa al final.
# ============================================================

tieneMasBultos = True
nroBulto = 1
valorPagarPorKilo = 0
valorPesoLiviano = 1000
valorPesoNormal = 4500
totalLiviano = 0
totalNormal = 0
contadorBultosLivianos = 0
contadorBultosNormales = 0

cantidadBultos = int(input("Ingrese cantidad de bultos: "))

# ↓ Condición: mientras el número de bulto no supere el total ingresado
# La variable nroBulto crece con cada vuelta (nroBulto += 1 al final)
# Cuando nroBulto > cantidadBultos, la condición es False y el ciclo para
while nroBulto <= cantidadBultos:
    try:
        pesoBulto = int(input(f"Ingrese el peso (1 a 10kg) del bulto Nro. {nroBulto}: "))
    except ValueError:
        # continue: salta el resto del bloque (incluye el nroBulto += 1)
        # y vuelve a evaluar la condición del while
        # Así el bulto con dato malo se puede reingresar sin perder el turno
        print("Peso del bulto debe estar en el rango de 1 y 10kg.")
        continue

    if 1 <= pesoBulto <= 5:
        totalLiviano += valorPesoLiviano
        contadorBultosLivianos += 1
    elif 6 <= pesoBulto <= 10:
        totalNormal += valorPesoNormal
        contadorBultosNormales += 1
    else:
        print("Peso ingresado incorrecto (1 - 10kg)")

    nroBulto += 1  # ← sin esta línea el ciclo sería infinito

# ─────────────────────────────────────────────────────────────
# EQUIVALENTE con while True (para comparar)
# ─────────────────────────────────────────────────────────────
# El mismo programa podría escribirse así:
#
#   while True:
#       if nroBulto > cantidadBultos:
#           break               ← condición de salida manual
#       pesoBulto = int(input(...))
#       ...
#       nroBulto += 1
#
# Ambas versiones hacen lo mismo. La diferencia es estética:
# - while condicion:  → la salida está visible desde la primera línea
# - while True+break → la salida está dentro del bloque (más oculta)
# Para este caso, "while nroBulto <= cantidadBultos" es más claro.
# ─────────────────────────────────────────────────────────────

print(f"Total a pagar por bultos livianos: {totalLiviano}")
print(f"Total a pagar por bultos normales: {totalNormal}")
print(f"Cantidad de bultos livianos: {contadorBultosLivianos}")
print(f"Cantidad de bultos normales: {contadorBultosNormales}")
