# EJERCICIO: AGENDA TELEFONICA SIMPLE
#
# Objetivo:
# Crear un programa que permita guardar hasta 3 contactos.
contacto1="No registrado"
tel1="No registrado"
contacto2="No registrado"
tel2="No registrado"
contacto3="No registrado"
tel3="No registrado"
# El menu debe mostrar:
while True:
    try:
        print("**AGENDA TELEFONICA SIMPLE**")
        print("*1. Agregar contacto")
        print("*2. Buscar contacto por nombre")
        print("*3. Mostrar contactos registrados")
        print("*4. Eliminar contacto")
        print("*5. Salir")
        op=int(input(" SU OPCION: "))
        if op==1:
            if contacto1=="No registrado":
                contacto1=input("Ingrese nombre del Contacto: ").strip()

                # CORRECCION: validar telefono (solo digitos y largo 9) sin funciones.
                while True:
                    tel1=input("Ingrese numero de telefono -9 digitos-: ").strip()
                    if not tel1.isdigit():
                        print("Debe ingresar solo digitos")
                    elif len(tel1)!=9:
                        print("El telefono debe tener 9 digitos")
                    else:
                        break
            elif contacto2=="No registrado":
                contacto2=input("Ingrese nombre del Contacto: ").strip()

                # CORRECCION: validar telefono (solo digitos y largo 9) sin funciones.
                while True:
                    tel2=input("Ingrese numero de telefono -9 digitos-: ").strip()
                    if not tel2.isdigit():
                        print("Debe ingresar solo digitos")
                    elif len(tel2)!=9:
                        print("El telefono debe tener 9 digitos")
                    else:
                        break
            elif contacto3=="No registrado":
                contacto3=input("Ingrese nombre del Contacto: ").strip()

                # CORRECCION: validar telefono (solo digitos y largo 9) sin funciones.
                while True:
                    tel3=input("Ingrese numero de telefono -9 digitos-: ").strip()
                    if not tel3.isdigit():
                        print("Debe ingresar solo digitos")
                    elif len(tel3)!=9:
                        print("El telefono debe tener 9 digitos")
                    else:
                        break
            else:
                if contacto3!="No registrado" and contacto1!="No registrado" and contacto2!="No registrado":
                    print("lo siento no se pueden guardar mas contactos")
        elif op==2:
            print("*menu de busqueda de contacto")
            busqueda=input("BUSCAR CONTACTO: ")
            if busqueda==contacto1:
                print("*Contacto encontrado!")
                print(f"Nombre:{contacto1}")
                print(f"Telefono:{tel1}")
            elif busqueda==contacto2:
                print("*Contacto encontrado!")
                print(f"Nombre:{contacto2}")
                print(f"Telefono:{tel2}")            
            elif busqueda==contacto3:
                print("*Contacto encontrado!")
                print(f"Nombre:{contacto3}")
                print(f"Telefono:{tel3}")
            else:
                print("No se encontro el contacto que busca :(, vuelva a ingresar al menu")
                continue
        elif op==3:
            print("*Contactos registrados")
            print("*Actualmente estos son los contactos registrados: ")
            if contacto1=="No registrado" and contacto2=="No registrado" and contacto3=="No registrado":
             print("Actualmente no hay contactos registrados, ingrese uno mediante el menu")
             continue
            elif contacto1!="No registrado" and contacto2=="No registrado" and contacto3=="No registrado":
             print(f"{contacto1}")
            elif contacto1!="No registrado" and contacto2!="No registrado" and contacto3=="No registrado":
             print(f"{contacto1}")
             print(f"{contacto2}")
            elif contacto1!="No registrado" and contacto2!="No registrado" and contacto3!="No registrado":
             print(f"{contacto1}")
             print(f"{contacto2}")
             print(f"{contacto3}")
            input("presione ENTER para volver al menu")
        elif op==4:
            while True:
                print("*Eliminar contacto")
                eliminar=input(f"Que contacto desea eliminar? 1. {contacto1} 2.{contacto2} 3. {contacto3} 4. Salir: ")
                # CORRECCION: input() devuelve texto, por eso se compara con "1", "2", etc.
                if eliminar == "1":
                    contacto1="No registrado"
                    tel1="No registrado"
                elif eliminar =="2":
                    contacto2="No registrado"
                    tel2="No registrado"
                elif eliminar =="3":
                    contacto3="No registrado"
                    tel3="No registrado"                
                elif eliminar =="4":
                    print("Saliendo")
                    break
                else:
                    print("Seleccione una opcion valida")
                    continue
        elif op==5:
            print("PROGRAMA FINALIZADO")
            break
    except ValueError:
        print("Debe ingresar solo digitos")    
# 1. Agregar contacto
# 2. Buscar contacto por nombre
# 3. Mostrar contactos registrados
# 4. Eliminar contacto
# 5. Salir
#
# Reglas:
# - Cada contacto debe tener nombre y telefono.
# - El telefono debe tener 9 digitos.
# - No se debe repetir el nombre de un contacto.
# - Solo se pueden guardar 3 contactos como maximo.
# - Debes resolverlo con variables separadas, por ejemplo: nombre1, telefono1, nombre2, telefono2, nombre3, telefono3.
# - El menu debe repetirse hasta que el usuario salga.
#
# Pistas:
# - Parte con variables en "No registrado", por ejemplo:
#   nombre1 = "No registrado"
#   telefono1 = "No registrado"
# - Cuando agregues un contacto, guarda primero en el espacio 1, luego en el 2 y luego en el 3.
# - Para evitar nombres repetidos, compara el nombre ingresado con nombre1, nombre2 y nombre3.
# - Para validar el telefono:
#   - Debe tener largo 9
#   - Debe contener solo numeros
# - Para mostrar los contactos, usa varios if y muestra solo los espacios que esten ocupados.
# - Para eliminar, busca el nombre y vuelve a dejar sus variables en "No registrado".
#
# Desafio extra:
# - Permite actualizar el telefono de un contacto existente.

# Escribe tu codigo debajo de estos comentarios.

# PISTAS EXTRA: COMO HACER LA BUSQUEDA (OPCION 2)
#
# Idea general:
# 1) Pides el nombre a buscar.
# 2) Comparas ese nombre con contacto1, contacto2 y contacto3.
# 3) Si coincide en alguno, muestras el telefono correspondiente.
# 4) Si no coincide en ninguno, avisas que no existe.
#
# Paso a paso sugerido:
# - Crea una variable para guardar lo que escribe el usuario:
#   nombre_buscado = input("Ingrese nombre a buscar: ")
#
# - Crea una variable bandera para saber si fue encontrado:
#   encontrado = False
#
# - Compara uno por uno:
#   if nombre_buscado == contacto1:
#       print(tel1)
#       encontrado = True
#   elif nombre_buscado == contacto2:
#       print(tel2)
#       encontrado = True
#   elif nombre_buscado == contacto3:
#       print(tel3)
#       encontrado = True
#
# - Al final, si no fue encontrado:
#   if encontrado == False:
#       print("Contacto no registrado")
#
# Consejos para que no falle:
# - Antes de comparar, revisa que el nombre guardado no sea "No registrado".
# - Si quieres evitar problemas de mayusculas/minusculas, compara con lower().
#   Ejemplo: nombre_buscado.lower() == contacto1.lower()
# - Si el usuario solo presiona ENTER, muestra mensaje y vuelve a pedir.