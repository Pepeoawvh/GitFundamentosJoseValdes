# Ejercicio de Práctica: Sistema de Gestión de Ítems
## Mercado de Prontera (Ragnarok Online)

> **Nota:** Este ejercicio combina a propósito los tres patrones que ya trabajaste:
> - La acumulación por categoría de **Ejercicio Extra (StreamFly)**.
> - El paso obligatorio de diccionarios como parámetros y la función `buscar_codigo()` reutilizable de **Taller (FlorExpress)** y **Consolas**.
> - El recorrido cruzado para mostrar el catálogo completo de **Consolas**.
>
> Intenta resolverlo tú solo/a antes de pedirme ayuda. Cuando tengas tu código, lo revisamos juntos.

## Contexto

En el MMORPG *Ragnarok Online*, el Mercado de Prontera es el punto donde los jugadores compran y venden ítems entre sí. Se requiere un programa en Python que administre el catálogo de ítems disponibles y su información comercial. Todo el comportamiento del sistema debe organizarse en funciones bien definidas, con un menú interactivo, validaciones de entrada y separación clara entre la lógica de cada función y las decisiones del programa principal.

## 1. Datos que debe manejar el sistema

El sistema trabaja con dos diccionarios relacionados, ambos identificados por el mismo **código de ítem** como clave. Deben existir desde que el programa inicia y permanecer disponibles durante toda la ejecución.

### Diccionario `items`

| Campo | Qué representa | Restricción de validación |
|---|---|---|
| `nombre` | Nombre del ítem | No debe estar vacío ni contener solo espacios en blanco |
| `tipo` | Categoría del ítem (Arma, Armadura, Accesorio, Consumible, Carta) | No debe estar vacío ni contener solo espacios en blanco |
| `clase_requerida` | Clase de personaje que puede equiparlo (ej: Swordsman, Mage, Archer, Acolyte, Todas) | No debe estar vacío ni contener solo espacios en blanco |
| `rareza` | Nivel de rareza del ítem | Debe ser exactamente `'Normal'`, `'Raro'`, `'Epico'` o `'Legendario'` |
| `comerciable` | Indica si el ítem se puede intercambiar entre jugadores | El usuario ingresa `'s'` o `'n'`. El sistema lo convierte a `True` o `False` |

```python
items = {
    'ITM001': ['Espada Sacra', 'Arma', 'Swordsman', 'Epico', True],
    'ITM002': ['Manto de Poring', 'Armadura', 'Todas', 'Normal', True],
    'ITM003': ['Carta Baphomet', 'Carta', 'Todas', 'Legendario', False],
    'ITM004': ['Pocion Azul', 'Consumible', 'Todas', 'Normal', True],
    'ITM005': ['Arco del Cazador', 'Arma', 'Archer', 'Raro', True]
}
```

### Diccionario `mercado`

| Campo | Qué representa | Restricción de validación |
|---|---|---|
| `precio_zeny` | Precio de venta en zeny (moneda del juego) | Número entero mayor que cero |
| `stock` | Unidades disponibles en el mercado | Número entero mayor o igual a cero |

```python
mercado = {
    'ITM001': [850000, 2],
    'ITM002': [12000, 15],
    'ITM003': [5000000, 1],
    'ITM004': [50, 200],
    'ITM005': [95000, 0]
}
```

## 2. Restricciones técnicas obligatorias

- Ambos diccionarios deben crearse en el programa principal y **pasarse como argumento** a todas las funciones que necesiten leerlos o modificarlos, aunque no se mencione explícitamente en cada opción. **No está permitido** acceder a ellos como variables globales dentro de las funciones.
- Cada estructura de repetición (`while`, `for`) debe usarse según su propósito natural: `while` cuando la condición de corte cambia durante la ejecución (por ejemplo, el ciclo del menú o el "¿desea continuar? s/n"), `for` cuando el volumen de iteraciones se conoce de antemano (por ejemplo, recorrer un diccionario completo).
- Las funciones de validación reciben **únicamente** el dato a validar, aplican su condición y retornan `True` o `False`. **No imprimen mensajes.** Los mensajes de error se muestran en la función o el bloque que solicita el dato.

## 3. Menú principal

```
========== MERCADO DE PRONTERA ==========
1. Stock total por tipo de ítem
2. Búsqueda de ítems por rango de precio
3. Actualizar precio de un ítem
4. Agregar nuevo ítem
5. Eliminar ítem
6. Mostrar catálogo completo
7. Salir
==========================================
```

Si el usuario ingresa una opción que no corresponde a ninguna válida, el sistema muestra `"Debe seleccionar una opción válida"` y vuelve a mostrar el menú.

Define una función `leer_opcion()`. No recibe parámetros. Solicita al usuario que ingrese una opción, valida que sea un número entero y que esté dentro del rango 1-7, y retorna ese valor entero. Si el usuario ingresa un dato que no es entero, debe manejarlo mediante excepciones (`try`/`except`).

## 4. Descripción detallada de cada opción

### Opción 1 — Stock total por tipo de ítem

Solicita al usuario un tipo de ítem (por ejemplo: arma, armadura, carta). La búsqueda **no distingue mayúsculas y minúsculas**. El sistema recorre `items` identificando los que correspondan a ese tipo, busca su código en `mercado`, extrae el stock (segundo elemento de la lista) y lo acumula. Muestra el total acumulado en pantalla.

- Función: `total_stock_tipo(tipo, items, mercado)`. No retorna valor, imprime el resultado directamente.

### Opción 2 — Búsqueda de ítems por rango de precio

Solicita un precio mínimo y un precio máximo. Recorre `mercado` y construye una lista con los ítems que **(a)** tengan precio dentro del rango **y (b)** tengan stock disponible (stock distinto de cero). Cada elemento tiene el formato `"Nombre--Código"`. Los resultados se muestran ordenados alfabéticamente por nombre. Si no hay resultados: `"No hay ítems disponibles en ese rango de precios."`

- Restricción de entrada: los valores deben ser enteros, validados en el programa principal con manejo de excepciones. Si el dato no es un entero válido: `"Debe ingresar valores enteros"`, y se vuelve a solicitar ambos valores.
- Función: `buscar_por_precio(precio_min, precio_max, items, mercado)`. Recibe el rango (`precio_min >= 0`, `precio_min <= precio_max`), no retorna valor, imprime los resultados.

### Opción 3 — Actualizar precio de un ítem

Solicita el código del ítem y el nuevo precio. Si el código existe, actualiza el precio. Si no, informa al usuario. Al terminar, pregunta: `"¿Desea actualizar otro ítem? (s/n)"`; si es `"s"` se repite, si es `"n"` vuelve al menú.

- Define `buscar_codigo(codigo, items)` que recorra el diccionario y retorne `True` si el código existe, `False` si no (sin distinguir mayúsculas/minúsculas).
- Define `actualizar_precio(codigo, nuevo_precio, items, mercado)`, que internamente invoque `buscar_codigo` (evita duplicar lógica de búsqueda). Si existe, actualiza el precio en `mercado` y retorna `True`. Si no, retorna `False`. El nuevo precio debe ser un entero positivo.
- El programa principal decide el mensaje **basándose exclusivamente en el valor retornado**: `"Precio actualizado"` o `"El código no existe"`.

### Opción 4 — Agregar nuevo ítem

Solicita todos los datos del nuevo ítem: código, nombre, tipo, clase requerida, rareza, si es comerciable, precio y stock. Cada dato se valida de forma independiente antes de crear el registro.

| Campo solicitado | Condición de validación |
|---|---|
| código | No vacío ni solo espacios, y que no exista ya (reutiliza `buscar_codigo`) |
| nombre | No vacío ni solo espacios en blanco |
| tipo | No vacío ni solo espacios en blanco |
| clase_requerida | No vacío ni solo espacios en blanco |
| rareza | Debe ser exactamente `'Normal'`, `'Raro'`, `'Epico'` o `'Legendario'` |
| comerciable | `'s'` o `'n'` → `True` o `False` |
| precio | Número entero mayor que cero |
| stock | Número entero mayor o igual a cero |

- Define una función de validación independiente por cada campo (pueden reutilizar la misma función de texto para varios campos si aplica la misma regla).
- Si todos los datos son válidos y el código no existe, el programa llama a `agregar_item(codigo, nombre, tipo, clase_requerida, rareza, comerciable, precio, stock, items, mercado)`, que agrega el registro a ambos diccionarios y retorna `True`. Si el código ya existía, retorna `False`.

### Opción 5 — Eliminar ítem

Solicita el código a eliminar. Si existe, lo elimina de ambos diccionarios e informa éxito. Si no, informa al usuario.

- Define `eliminar_item(codigo, items, mercado)`, que reutiliza `buscar_codigo` internamente (sin duplicar su lógica). Si existe, elimina de ambos diccionarios y retorna `True`. Si no, retorna `False`.
- El principal decide el mensaje según el valor retornado: `"Ítem eliminado"` o `"El código no existe"`.

### Opción 6 — Mostrar catálogo completo

Recorre ambos diccionarios de forma cruzada mediante la clave compartida y muestra la información combinada de cada ítem. Si no hay ítems registrados: `"El mercado no tiene ítems registrados."`

Formato esperado:
```
==============================
CATÁLOGO DEL MERCADO
==============================
ITM001 | Espada Sacra | Arma | Epico | $850,000 zeny | Stock: 2
ITM002 | Manto de Poring | Armadura | Normal | $12,000 zeny | Stock: 15
==============================
Total de ítems: 2
```

- Función: `mostrar_catalogo(items, mercado)`.

### Opción 7 — Salir

El ciclo del menú se detiene y el programa finaliza mostrando: `"Programa finalizado."`

## 5. Ejemplo de ejecución

```
========== MERCADO DE PRONTERA ==========
1. Stock total por tipo de ítem
2. Búsqueda de ítems por rango de precio
3. Actualizar precio de un ítem
4. Agregar nuevo ítem
5. Eliminar ítem
6. Mostrar catálogo completo
7. Salir
==========================================
Ingrese opción: 1
Ingrese tipo de ítem a consultar: arma
El stock total disponible es: 2 unidades.

Ingrese opción: 2
Ingrese precio mínimo: hola
Debe ingresar valores enteros
Ingrese precio mínimo: 10000
Ingrese precio máximo: 900000
Los ítems encontrados son: ['Espada Sacra--ITM001', 'Manto de Poring--ITM002']

Ingrese opción: 3
Ingrese código del ítem: ITM099
Ingrese nuevo precio: 20000
El código no existe
¿Desea actualizar otro ítem? (s/n): n

Ingrese opción: 4
Ingrese código del ítem: ITM006
Ingrese nombre: Alas de Angel
Ingrese tipo: Accesorio
Ingrese clase requerida: Todas
Ingrese rareza (Normal/Raro/Epico/Legendario): Legendario
¿Es comerciable? (s/n): n
Ingrese precio en zeny: 15000000
Ingrese stock: 1
Ítem agregado con éxito.

Ingrese opción: 6
==============================
CATÁLOGO DEL MERCADO
==============================
ITM001 | Espada Sacra | Arma | Epico | $850,000 zeny | Stock: 2
ITM002 | Manto de Poring | Armadura | Normal | $12,000 zeny | Stock: 15
ITM003 | Carta Baphomet | Carta | Legendario | $5,000,000 zeny | Stock: 1
ITM004 | Pocion Azul | Consumible | Normal | $50 zeny | Stock: 200
ITM005 | Arco del Cazador | Arma | Raro | $95,000 zeny | Stock: 0
ITM006 | Alas de Angel | Accesorio | Legendario | $15,000,000 zeny | Stock: 1
==============================
Total de ítems: 6

Ingrese opción: 7
Programa finalizado.
```
