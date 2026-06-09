# # El complejo educacional “Chile 2030”, desea realizar una aplicación computacional que le permita registrar en sus establecimientos los alumnos a sus cursos.

# # Por tal razón le ha solicitado que cree un programa que le permita a coordinación estudiantil registrar los alumnos que pertenezcan a un curso en particular.
# El complejo educacional “Chile 2030”, desea realizar una aplicación computacional que le permita registrar en sus establecimientos los alumnos a sus cursos.

# Por tal razón le ha solicitado que cree un programa que le permita a coordinación estudiantil registrar los alumnos que pertenezcan a un curso en particular.

# Como prototipo, usted desarrolla un algoritmo que permite almacenar un número variable de alumnos a un curso, pero con un máximo de 30 por curso.

# Construya el código que responda a los siguientes resultados:
cursos=[]
alumno=[]
nombre=""
cont=0


while True:
    while True:
        nombre=input("Ingrese el nombre del alumno: ").upper()
        if nombre.isalpha():
            print("Nombre registrado")
            break
        elif nombre=="":
            print("No puede dejar el nombre vacio")
            continue
        elif nombre in cursos:
            print("El nombre ya existe en el curso")
            continue
        elif nombre.isnumeric():
            print("Quien tiene nombre de numeros aparte de los hijos de un magnate extravagante de sudafrica")
            continue
        else:
            print("Error al ingresar el nombre verifique que sean solo letras")
            continue
    while True:
        direccion=input("Ingrese direccion del alumno: ")
        if direccion=="":
            print("Debe ingresar la direccion del alumno")
            continue
        else:
            break
    while True:
        telefono=int(input("Ingrese telefono del estudiante: "))
        
    