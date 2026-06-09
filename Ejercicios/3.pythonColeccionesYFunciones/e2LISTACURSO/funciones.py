
# Validar todos los datos ingresados por el usuario.
# Validaciones obligatorias

#  Si no existen alumnos registrados, las opciones mostrar, promedios, mejor alumno y aprobados deben
# indicarlo correctamente.
#  Usar funciones para cada opcion del menu.
# Funciones obligatorias

estudiantes={}

nombre=""
nota=0
promedio=0
def agregar_alumno(estudiantes):
    while True:      
        nombre=input("Ingrese nombre de estudiante: ")
        if nombre in estudiantes:
            print("Ya existe el estudiante, reintente")
            continue
        elif nombre == "":
            print("No puede dejar el campo vacio, reintente")
            continue
        elif nombre.isalpha():
            estudiantes[nombre]=[]
            try:
                cantNotas=int(input("Ingrese la cantida de notas a ingresar: "))
                if cantNotas <=0:
                    print("Debe ingresar un numero mayor a 0")
                    continue
                else:
                    for i in range(cantNotas):
                        while True:
                            try:
                                nota=float(input(f"Ingrese nota {i+1} en formato 0.0: "))
                                if nota < 1.0 or nota > 7.0:
                                    print("La nota debe ser entre 1.0 y 7.0 reintente")
                                    continue
                                elif nota >= 1.0 and nota <= 7.0:
                                    estudiantes[nombre].append(nota)
                                    return
                            except ValueError:
                                print("Debe ingresar notas con decimal")    
                                continue
                print(f"Se ingresaron correctamente las notas de {nombre}")
            except ValueError:
                print("Debe ingresar numeros enteros positivos")
        else:
            print("El nombre solo puede contener letras") 
#  El nombre del alumno no puede estar vacio.
#  Agregar alumnos solicitando nombre, cantidad de notas y notas.
#  La cantidad de notas debe ser un numero entero mayor que 0.
#  Cada nota debe estar entre 1.0 y 7.0.
#  No se debe permitir agregar un alumno repetido.
def mostrar_alumnos(estudiantes):
    print(f"Esta es la lista de estudiantes  y sus notas {estudiantes}")
    
def ver_promedios(estudiantes):
        
        if not estudiantes:
            print("no hay alumnos registrados")
            return #para devolver que no existen alumnos registrados cuando se llame a la funcion
        for nombre in estudiantes:
            promedio=sum(estudiantes[nombre])/(len(estudiantes[nombre]))
            print(f"{nombre}: promedio {promedio:.1f}")
            
            
#  Calcular y mostrar el promedio de cada alumno.
def mejor_alumno(estudiantes):
    mejorNombre=""
    mejorPromedio=0
    if not estudiantes:
        print("No hay estudiantes registrados")
        return
    for nombre, notas in estudiantes.items():
        promedio=sum(notas)/(len(notas))
        if promedio > mejorPromedio:
            mejorPromedio=promedio
            mejorNombre=nombre
    print(f"El mejor alumno es {mejorNombre} con promedio {mejorPromedio:.1f}")
    
    
def cantidad_aprobados(estudiantes):
    aprobados=0
    for nombre in estudiantes:
        promedio= sum(estudiantes[nombre])/len(estudiantes[nombre])
        if promedio >= 4.0:
            aprobados = aprobados+1
    print(f"actualmente hay {aprobados} alumnos aprobados")
#  Mostrar la cantidad de alumnos aprobados. Se considera aprobado si su promedio es mayor o igual a
# 4.0.






# Desafio opcional
#  Modificar datos existentes.
#  Eliminar registros.
#  Ordenar productos o alumnos segun precio o promedio.
#  Mostrar estadisticas generales.