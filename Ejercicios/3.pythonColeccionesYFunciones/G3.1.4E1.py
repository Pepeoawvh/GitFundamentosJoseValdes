# # El complejo educacional “Chile 2030”, desea realizar una aplicación computacional que le permita registrar en sus establecimientos los alumnos a sus cursos.

# # Por tal razón le ha solicitado que cree un programa que le permita a coordinación estudiantil registrar los alumnos que pertenezcan a un curso en particular.
# El complejo educacional “Chile 2030”, desea realizar una aplicación computacional que le permita registrar en sus establecimientos los alumnos a sus cursos.

# Por tal razón le ha solicitado que cree un programa que le permita a coordinación estudiantil registrar los alumnos que pertenezcan a un curso en particular.

# Como prototipo, usted desarrolla un algoritmo que permite almacenar un número variable de alumnos a un curso, pero con un máximo de 30 por curso.

# Construya el código que responda a los siguientes resultados:
cursos=[]
cont=0
def ingresoAlumno(cont,cursos):
    alumno=[]
    nombre=""
    if cont==30:
        print("Las matriculas estan llenas")
        return
    while True:
        while True:
            nombre=input("Ingrese el nombre del alumno: ").upper()
            if nombre=="":
                print("No puede dejar el nombre vacio")
                continue
            elif nombre in cursos:
                print("El nombre ya existe en el curso")
                continue
            elif nombre.isnumeric():
                print("Quien tiene nombre de numeros aparte de los hijos de un magnate extravagante de sudafrica")
                continue
            elif nombre.isalpha():
                print("Nombre registrado")
                while True:
                    direccion=input("Ingrese direccion del alumno: ")
                    if direccion==" ":
                        print("Debe ingresar la direccion del alumno")
                        continue
                    else:
                        while True:
                            telefono=(input("Ingrese telefono del estudiante: "))          
                            if len(telefono) != 8 and telefono.isnumeric():
                                print("el telefono debe tener 8 digitos")
                                continue
                            elif any(caracter.isalpha() for caracter in telefono):
                                print("el telefono solo debe contener numeros")
                                continue
                            else:
                                alumno=[nombre,direccion,telefono]
                                cursos.append(alumno)
                                cont=cont+1
                                print("El usuario se ha ingresado correctamente")
                                for alumno in cursos:
                                    print(f"Estudiante {cont + 1}")
                                    print("Nombre: " ,alumno[0])
                                    print("Dirección: ", alumno[1])
                                    print("Teléfono: ", alumno[2])
                                    print("")
                                return cont
while True:
    cont=ingresoAlumno(cont,cursos)                                 
    if cont==30:
        print("No se pueden ingresar mas usuarios")
        break


    