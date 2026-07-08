Instrucciones del Ejercicio: "Sistema de Gestión de Streaming
(StreamFly)"
La plataforma de streaming StreamFly requiere un programa en Python para
administrar su catálogo de series y sus métricas de visualización.
Todo el comportamiento del sistema debe organizarse en funciones bien definidas.
El programa incluye un menú interactivo, validaciones de entrada y una
separación clara entre la lógica de cada función y las decisiones del programa
principal.
1. Datos que debe manejar el sistema
El sistema trabaja con dos diccionarios relacionados, ambos identificados por el
mismo código de serie como clave. Estos diccionarios deben existir desde que el
programa inicia y permanecer disponibles durante toda la ejecución.
Diccionario peliculas
Contiene la información descriptiva de cada serie o película. La clave es el código
de la serie y el valor es una lista con los siguientes campos, en este orden:
Campo Qué representa Restricciones de validación
titulo Nombre de la serie No debe contener solo espacios
en blanco ni estar vacío
plataforma Plataforma original en No debe contener solo espacios
que se transmite en blanco ni estar vacío
genero Género de la producción No debe contener solo espacios
en blanco ni estar vacío
clasificacio Clasificación de edad Debe ser exactamente 'TEEN' o
n '18+'
original Indica si es producción El usuario ingresa 's' o 'n'. El
propia de la plataforma sistema lo convierte a True o
False

Python
peliculas = {
'S001': ['Stranger Things', 'Netflix', 'Ciencia Ficcion', 'TEEN', True],
'S002': ['The Mandalorian', 'Disney+', 'Sci-Fi', 'TEEN', False],
'S003': ['The Boys', 'Prime Video', 'Accion', '18+', False]
}
Diccionario metricas
Contiene la información operativa de cada serie. La clave es el mismo código de
serie y el valor es una lista con los siguientes dos campos:
Campo Qué representa Restricciones de validación
precio_arriend Costo de arriendo digital en Número entero mayor o igual
o pesos a cero
reproduccione Cantidad de vistas en miles Número entero mayor o igual
s a cero
Python
metricas = {
'S001': [0, 450],
'S002': [2500, 120],
'S003': [0, 890]
}
2. Lo que debe hacer el sistema
El sistema se controla desde un menú que aparece en pantalla cada vez que el
usuario termina una acción. El usuario elige una opción numérica, el programa
ejecuta la tarea correspondiente y vuelve a mostrar el menú. Esto se repite hasta
que el usuario elige salir. Si el usuario ingresa un valor que no corresponda a
ninguna opción válida, el sistema muestra el mensaje "Debe seleccionar una
opción válida" y vuelve a mostrar el menú.
Plaintext
========== MENÚ PRINCIPAL ==========
1. Total de reproducciones por plataforma
2. Búsqueda de series por rango de vistas
3. Actualizar precio de arriendo
4. Agregar nueva serie
5. Eliminar serie
6. Salir
=====================================
A continuación, se describe qué debe ocurrir al elegir cada opción:

Opción 1 — Total de reproducciones por plataforma
El sistema solicita al usuario el nombre de una plataforma (por ejemplo: Netflix,
Disney+ o Prime Video). La búsqueda no distingue entre mayúsculas y
minúsculas, por lo que "netflix" y "Netflix" deben producir el mismo resultado.
El sistema recorre el diccionario peliculas identificando todas las series que
pertenezcan a esa plataforma. Por cada serie que cumpla con la condición, se
debe buscar su código en el diccionario metricas, extraer su cantidad de
reproducciones (el segundo elemento de la lista) y acumularla en un total. Una vez
procesados todos los elementos encontrados, se debe mostrar dicho total
acumulado en pantalla.
● Para implementar esta opción: Define una función llamada
total_reproducciones(plataforma). Recibe la plataforma como parámetro, no
retorna ningún valor y muestra el resultado directamente por pantalla.
Opción 2 — Búsqueda de series por rango de vistas
El sistema solicita al usuario un mínimo y un máximo de reproducciones (en
miles). Luego recorre el diccionario metricas y construye una lista con todas las
series que tengan una cantidad de vistas dentro del rango ingresado. Cada
elemento de la lista resultante tiene el formato "Titulo--Codigo". Los resultados se
muestran ordenados alfabéticamente por título de la serie. Si no hay series que
cumplan las condiciones, el sistema muestra: "No hay series en ese rango de
reproducciones."
● Restricciones de entrada: El rango mínimo y máximo deben ingresarse
como valores enteros. Esta validación ocurre en el programa principal,
antes de llamar a la función. Como el usuario puede ingresar cualquier tipo
de dato, debe utilizarse manejo de excepciones. Si el dato ingresado no es
un entero válido, el sistema muestra "Debe ingresar valores enteros" y
vuelve a solicitar ambos valores.
● Para implementar esta opción: Define una función llamada
buscar_por_vistas(min_vistas, max_vistas). Recibe el rango como
parámetro (los valores deben ser mayores o iguales a cero y el min_vistas
menor o igual al max_vistas), no retorna ningún valor y muestra los
resultados directamente por pantalla.
Opción 3 — Actualizar precio de arriendo
El sistema solicita al usuario el código de la serie y el nuevo precio que se desea
asignar. Si el código existe en el diccionario metricas, el sistema actualiza su
precio. Si el código no existe, informa al usuario. Al terminar, pregunta: "¿Desea
actualizar otro precio (s/n)?": si la respuesta es "s", el proceso se repite; si es
"n", el programa vuelve al menú principal.
● Para implementar esta opción: Define una función llamada
actualizar_precio(codigo, nuevo_precio). Si el código no existe, retorna
False. Si el código existe, actualiza el precio en el diccionario y retorna
True. El programa principal recibe ese valor y decide qué mostrar: "Precio
actualizado" o "El código no existe". La validación del código no debe
distinguir mayúsculas y minúsculas.

|     |                                              |     |
| --- | -------------------------------------------- | --- |
Opción 4 — Agregar nueva serie
El  sistema  solicita al  usuario todos los datos de la nueva serie: código, título,
plataforma, género, clasificación, si es original, precio y reproducciones. Antes de
crear el registro, cada dato es validado de forma independiente mediante una
función  dedicada. Si algún dato no cumple su condición, el sistema informa al
usuario y no registra la serie. Solo cuando todos los datos son válidos y el código
no existe previamente, el sistema agrega el registro en ambos diccionarios.
| Campo  Condición de validación  |     |     |
| ------------------------------- | --- | --- |
solicitado
código  No vacío ni solo espacios en blanco, y que no exista ya en
los diccionarios
| título  No vacío ni solo espacios en blanco         |     |     |
| --------------------------------------------------- | --- | --- |
| plataforma  No vacía ni solo espacios en blanco     |     |     |
| género  No vacío ni solo espacios en blanco         |     |     |
| clasificación  Debe ser exactamente 'TEEN' o '18+'  |     |     |
original  El usuario ingresa 's' o 'n'. El sistema almacena True si es
's', False si es 'n'
| precio  Número entero mayor o igual a cero          |     |     |
| --------------------------------------------------- | --- | --- |
| reproducciones  Número entero mayor o igual a cero  |     |     |
●
Para implementar esta opción: Define una función de validación
independiente para cada campo. Cada función recibe únicamente el dato a
validar, aplica su condición y retorna True si es válido o False si no lo es.
Los mensajes de error no se muestran dentro de las funciones de
validación.
●  En el programa principal, se solicitan los datos y se procesan las llamadas
a las validaciones. Si todas son correctas, el programa llama a la función

agregar_serie(codigo, titulo, plataforma, genero, clasificacion, original,
precio, reproducciones), la cual añade la información a ambos diccionarios
y retorna True. Si el código ya existía, retorna False.
Opción 5 — Eliminar serie
El sistema solicita el código de la serie que se desea eliminar. Si el código existe,
elimina el registro en ambos diccionarios (peliculas y metricas) e informa que la
operación fue exitosa. Si el código no existe, informa al usuario.
● Para implementar esta opción: Define una función llamada
eliminar_serie(codigo). Si el código no existe en los diccionarios, retorna
False. Si existe, lo remueve de ambos y retorna True. La validación del
código no distingue mayúsculas y minúsculas.
Opción 6 — Salir
El sistema termina la ejecución de forma limpia. El ciclo del menú se detiene y el
programa finaliza mostrando el mensaje: "Programa finalizado."
3. Ejemplo de ejecución
Los datos en negrita son valores ingresados por el usuario ficticio:
Plaintext
========== MENÚ PRINCIPAL ==========
1. Total de reproducciones por plataforma
2. Búsqueda de series por rango de vistas
3. Actualizar precio de arriendo
4. Agregar nueva serie
5. Eliminar serie
6. Salir
=====================================
Ingrese opción: 1
Ingrese plataforma a consultar: netflix
El total de reproducciones acumuladas es: 450 mil.
Ingrese opción: 2
Ingrese vistas mínimas (en miles): hola
Debe ingresar valores enteros
Ingrese vistas mínimas (en miles): 100
Ingrese vistas máximas (en miles): 500
Las series encontradas son: ['Stranger Things--S001', 'The Mandalorian--S002']
Ingrese opción: 3
Ingrese código de la serie: S999
Ingrese nuevo precio: 1500
El código no existe
¿Desea actualizar otro precio (s/n)?: n
Ingrese opción: 4
Ingrese código de la serie: S004
Ingrese título: Better Call Saul
Ingrese plataforma: AMC
Ingrese género: Drama
Ingrese clasificación: 18+

¿Es original? (s/n): n
Ingrese precio de arriendo: 1990
Ingrese reproducciones (en miles): 320
Serie agregada con éxito.
Ingrese opción: 6
Programa finalizado.