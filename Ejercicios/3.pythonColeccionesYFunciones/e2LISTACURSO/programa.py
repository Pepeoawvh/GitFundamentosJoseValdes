import funciones as fn
estudiantes={}
# Una academia necesita un programa en Python para registrar alumnos y sus notas. La informacion debe
# almacenarse en un diccionario.
# Estructura sugerida
# alumnos = {
# "Ana": [5.5, 6.0, 4.8],
# "Luis": [3.9, 4.1, 5.0],
# "Pedro": [6.5, 6.8, 7.0]
# }
# En esta estructura, la clave corresponde al nombre del alumno y el valor es una lista con sus notas.
# Menu requerido
# 1. Agregar alumno
# 2. Mostrar alumnos
# 3. Ver promedios
# 4. Mejor alumno
# 5. Cantidad de aprobados
# 6. Salir
# Requerimientos
# 
#  La opcion del menu debe estar entre 1 y 6.
while True:
    try:
        print("------MENU DE GESTION DE CURSO------")
        print("1. Agregar alumno")
        print("2. Mostrar alumno")
        print("3. Ver promedios")
        print("4. Mejor Alumno")
        print("5. Cantidad de aprobados")
        print("6. Salir")
        opMenu=int(input("Ingrese su opcion: "))
        if opMenu <= 0 or opMenu >= 7:
            print("Debe ingresar una opcion valida del menu")
            continue
        else:
            if opMenu ==1:
                print("-----AGREGAR ALUMNO-----")
                fn.agregar_alumno(estudiantes)
            elif opMenu ==2:
                print("----MOSTRAR ALUMNOS----")
                if not estudiantes:
                    print("No no hay ningun estudiante registrado, agregue al menos uno")
                    continue
                else:
                    fn.mostrar_alumnos(estudiantes)
            elif opMenu==3:
                print("----VER PROMEDIOS----")
                fn.ver_promedios(estudiantes)
            elif opMenu==4:
                print("----MEJOR PROMEDIO----")
                fn.mejor_alumno(estudiantes)
            elif opMenu==5:
                print('----Cantidad de Aprobados----')
                fn.cantidad_aprobados(estudiantes)
            
                
            
    except ValueError:
        print("valor ingresado es invalido")