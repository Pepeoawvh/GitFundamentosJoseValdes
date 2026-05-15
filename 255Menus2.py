
usuario1=None 
usuario2=None 
usuario3=None
contrasena1= None 
contrasena2=None 
contrasena3= None

while True:
    try:   
        print("*****************")
        print("*Menu de inicio*")
        print("1) Iniciar Sesion")
        print("2) Registrar Usuario")
        print("3) Salir")
        op=int(input("Ingrese su opción: "))
        if op > 3 or op < 1:
            print("Ingrese una opción del 1 al 3")

        elif op == 1:
            
            if usuario1==None and usuario2==None and usuario3==None:   
                print("*Es necesario registrar almenos un usuario antes de iniciar sesion, cree un usuario usando la opcion 2")
            else:
                print("*Menu de inicio de sesion*")
                user_log=input("Ingrese Usuario: ")                    
                pass_log=input("Ingrese Password: ")
                if (user_log == usuario1 and pass_log==contrasena1) or (user_log==usuario2 and pass_log==contrasena2) or (user_log==usuario3 and pass_log==contrasena3):
                    print("*Inicio de sesion exitoso")
                    while True:
                        try:
                            print("*****************************")
                            print("*Que deseas hacer?*")
                            print("1) Realizar llamada")
                            print("2) Enviar correo Electronico")
                            print("3) Cerrar sesion")
                            op=int(input("Ingrese su opcion: "))
                            if op!=1 or op!=2 or op!=3:
                                print("Debe ingresar una opcion valida, 1, 2,o 3")
                            else:
                                break
                        except ValueError:
                            print("Debe ingresar una opción valida, solo digitos")
                        if op==1:
                            while True:
                                try:
                                    print("********")
                                    print("*Realiza tu llamada*")
                                    telefono=(input("Ingrese numero telefonico: "))
                                    valid9=telefono.startswith("9")
                                    if valid9==True and len(telefono)==9:
                                        print("Telefono Valido, LLamando..... TUUUT TUUUT TUUUT")
                                        break
                                    elif telefono != valid9:
                                        print("*El telefono debe comenzar con el digito '9' y tener 9 digitos")
                                    elif len(telefono)!=9:
                                        print("*El telefono debe comenzar con el digito '9' y tener 9 digitos")                                         
                                    else:
                                        print("*Verifique formato del numero telefonico, debe comenzar con 9 y tener 9 digitos")
                                except ValueError:
                                    print("*Error, ingresa solo digitos para llamar")
                        elif op==2:
                            # La opción 2, solicita un correo electrónico, el cual debe tener por lo menos un carácter de “@” (validar usando for y while) y lo guardará en una variable llamada “correo”.
                            # También solicitará el mensaje a enviar y lo guardará en una variable llamada “mensaje”

                            while True:
                                print("******************")
                                print("*Envio de Correo Electronico")
                                email=(input("Ingrese Correo Destinatario: "))
                                if "@" in email:
                                    mensaje=(input("Ingrese el contenido del correo: "))
                                    print("Enviando...")
                                    print("Correo enviado!...")
                                    break   
                                else:
                                    print("El correo electronico debe tener contener un @")
                        elif op==3:
                            print("Cerrando Sesion...")
                            print("Sesion Cerrada")
                            break
                        else:
                            print("Debe ingresar una opcion valida: 1,2 o 3")
                            # Finalmente cerrar sesión, volverá al menú principal.                                                       
        elif op==2:
            print("*******************")
            print("*Registro de usuario*")
            if usuario1==None and contrasena1==None:
                usuario1=input("Ingrese usuario a registrar: ")
                contrasena1=input("Ingrese contraseña: ")    
                contrasena1=input("Ingrese contraseña nuevamente: ")
                print("*Usuario creado exitosamente, ahora puede iniciar sesion")
            elif usuario1!=None and contrasena1 != None:
                usuario2=input("Ingrese usuario a registrar: ")
                contrasena2=input("Ingrese contraseña: ")    
                contrasena2=input("Ingrese contraseña nuevamente: ")
                print("*Usuario creado exitosamente, ahora puede iniciar sesion")
            elif (usuario2!=None and contrasena2 != None) or (usuario1!=None and contrasena1 != None):
                usuario3=input("Ingrese usuario: ")
                contrasena3=input("Ingrese contraseña a registrar: ")    
                contrasena3=input("Ingrese contraseña nuevamente: ")
                print("*Usuario creado exitosamente, ahora puede iniciar sesion")
            else:
                print("Lo sentimos, no pueden registrarse mas usuarios")
        elif op==3:
            print("Saliendo, Chau")   
            break             
                          
    except ValueError:
        print("Error, ingrese solo digitos")

# El sistema no acepta que se ingresen opciones distintas a 1, 2 y 3 en ambos menús, si ocurre esto, entonces el sistema emite un error y vuelve a solicitar la opción.

# Recuerde utilizar try Exception en caso de ser necesario.
		
