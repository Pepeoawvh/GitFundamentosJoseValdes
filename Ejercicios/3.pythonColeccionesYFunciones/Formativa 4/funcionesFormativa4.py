usuarios={}
def agregarUsuario(usuarios):
    while True:      
        nombre=input("Ingrese nombre del usuario: ")
        if nombre in usuarios:
            print("***El usuario ya existe, reintente")
        elif nombre == "":
            print("***No puede dejar el campo vacio, reintente")
            continue
        elif nombre.isalpha():
            while True:
                sexo=input("Ingrese sexo: M o F: :").upper()
                if sexo=="M" or sexo=="F":
                    while True:
                        contrasena=input("Ingrese contrasena: ")
                        if len(contrasena)>=8 and any(caracter.isdigit() for caracter in contrasena) and any(caracter.isalpha() for caracter in contrasena) and not " " in contrasena:
                            usuarios[nombre]={"sexo":sexo,"contrasena":contrasena}
                            print("***Usuario creado exitosamente")
                            return
                        else:
                            print("***Contrasena debe tener minimo 8 caracteres, al menos un numero, almenos una letra y no puede tener espacios")
                            continue
                else:
                    print("***Debe ingresar M o F")
                    continue                        
        else:
            print("***El nombre debe ser solo letras")
            continue

def buscarUsuario(usuarios):
    busqueda=input("Ingrese el usuario a buscar:").strip().lower()
    if not usuarios:
        print("***La lista de usuarios esta vacia, registre uno primero")
    elif busqueda in usuarios and busqueda.isalpha():
         print(f"Usuario encontrado! {busqueda}: "f"sexo: {usuarios[busqueda]['sexo']}, "f"contrasena: {usuarios[busqueda]['contrasena']}"
)
    elif any(caracter.isdigit() for caracter in busqueda):
        print("***El nombre a buscar no puede contener numeros, reintente")
    else:
        print("***El usuario no existe, reintente")
        
def eliminarUsuario(usuarios):
    eliminable=input("Ingrese usuario a Eliminar: ")
    if not usuarios:
        print("***ERROR No hay usuarios registrados, registre uno")
    elif any(caracter.isdigit() for caracter in eliminable):
        print("***El nombre a buscar no puede contener numeros, reintente")
    elif eliminable=="":
        print("***debe escribir un nombre para ingresar, reintente")
    elif eliminable in usuarios and eliminable.isalpha():
         del usuarios[eliminable]
         print(f"usuario eliminado! {eliminable}")
    else:
        print("***No se pudo eliminar usuario")
         



# tarea: convertirlo a diccionarios