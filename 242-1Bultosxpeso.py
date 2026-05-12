# Realiza construcción de un programa que deba realizar lo siguiente:
 
# Comienza con la inicialización de variables y solicita al usuario la cantidad de bultos. 
try:
    print("***************************************")
    cant_bultos=int(input("ingrese cantidad de bultos: "))
    liviano=0
    normal=0
    preciol=1000
    precion=2000
    total=0
    
    
    for i  in range (cant_bultos):
        peso=int(input(f"Ingrese el peso del bulto N°{i+1}"))
        if peso >= 1 and peso<=5:
            print("Su paquete es Liviano")
            liviano=liviano+1
            total=total+preciol
        elif peso > 5  and peso <=10:
            print("Su paquete es normal")
            normal=normal+1
            total=total+precion
        elif peso > 10:
            print("No se permiten Bultos tan pesados, intentalo nuevamente")
    print("_________________")
    print("RESUMEN")
    print(f"{liviano} bultos livianos: ${preciol*liviano} ")
    print(f"{normal} bultos normales: ${precion*normal}")
    print(f"Total a pagar: ${total}")

except:
    print("Debe ingresar numeros")        
# Luego, utiliza un bucle FOR para procesar cada bulto, solicitando el peso al usuario y manejando posibles errores (agregar excepciones).
# 
# Dependiendo del peso ingresado, acumula valores y contadores correspondientes para bultos livianos y normales. Finalmente, imprime el total a pagar por bultos livianos y normales, así como la cantidad de bultos en cada categoría


# Una empresa de transporte requiere automatizar sus procesos de cálculo para poder cobrar por la cantidad de paquetes que trae un cliente.
# Para calcular el valor total a cobrar y catalogarlo para envío,  requiere preguntar el peso de cada bulto y determinar el valor según lo siguiente: 

# Kilos 1-5, categoria liviana valor 1000
# kilos 6-10 categoria  normal 2000





# Ejemplo:
# Si un cliente ingresa 3 bultos y según sus pesos estos clasifican en 1 liviano y 2 normales, el cliente debe paga $5,000
# El sistema debe mostrar lo siguiente:
# 1 bulto liviano $1,000
# 2 bultos normales $4,000
# Valor total a pagar: $5,000
