import funcionesFormativa4 as fn4
# Haga un programa que permita generar un menú de ingreso de usuarios. El menú principal debe permitir mostrar 3 opciones:

# 1.- Ingresar usuario.
# 2.- Buscar usuario.
# 3.- Eliminar usuario.
# 4.- Salir.
usuarios={}
# Al ingresar a la opción 1.-, se debe permitir ingresar nombre de usuario, sexo y contraseña por separado. Para que el ingreso del usuario sea exitoso se debe cumplir lo siguiente: a) el nombre de usuario no debe estar repetido, b) el sexo solo permite “F” o “M” y c) la contraseña debe ser de largo mínimo 8 caracteres, debe tener al menos 1 número, debe tener al menos 1 letra y no puede tener espacio en blanco. En caso de cumplir todas las condiciones, el usuario es ingresado exitosamente.
while True:
    print("----MENU DE INGRESO DE USUARIO----")
    print("1. Ingresar usuario")
    print("2. Buscar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")
    try:
        opMenu=int(input("Ingrese su opcion: "))
        if opMenu <1 or opMenu > 4:
            print("Debe ingresar una opcion entre 1 y 4")
            continue
        elif opMenu==1:
            print("----INGRESAR USUARIO----")
            fn4.agregarUsuario(usuarios)
        elif opMenu==2:
            print("----Buscar usuario----")
            fn4.buscarUsuario(usuarios)
        elif opMenu==3:
            print("----Eliminar Usuario----")
            fn4.eliminarUsuario(usuarios)
        elif opMenu==4:
            print("CHAU, vuelva pronto")
            break
    except ValueError:
        print("La opcion debe ser un numero")
    


        # Al ingresar la opción 2.-, el menú debe permitir buscar usuarios mediante el nombre de usuario. Si el usuario existe, debe mostrar los datos asociados al usuario: sexo y contraseña. Si el usuario no existe, debe mostrar un mensaje que el usuario no se encuentra.

# Al ingresar la opción 3.-, el menú debe permitir eliminar al usuario y toda la información asociada a este mediante el ingreso de un nombre de usuario por teclado. Si el usuario es eliminado, se debe mostrar un mensaje como: “Usuario eliminado!”, pero en caso de que el usuario no exista, se muestra un mensaje como: “No se pudo eliminar usuario!”.

# Al ingresar la opción 4.-, el programa debe terminar. 

# Si se ingresa una opción distinta, debe mostrar un mensaje que debe seleccionar una opción válida. Todas las opciones del menú deben estar implementas mediante funciones separadas del código principal (main).