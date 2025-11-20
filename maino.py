# Usamos de la libreria estandar de python la herramienta random para usar sus funciones aleatorias para generar obstaculos aleatorios.
import random

# Importa el modulo estandar de python "heapq", sirve para trabajar con colas de prioridad usando estructuras llamadas heaps(monticulos).
# Un "heap" es basicamente una lista que siempre mantiene el menor valor en la primera posicion, de forma que extrae el valor mas pequenho rapidamente.  
import heapq


# ================================= BLOQUE DE FUNCIONES ============================================================== #

# Definimos la primera funcion que crea la matriz base del mapa(Una matriz de ceros) con parametros de fila y columna.
def generar_matriz(filas,columnas):

    # Retornamos la generacion de la matriz utilizando la comprension de listas.
    # El lugar del cero es el valor que queramos que sea la matriz, en este caso una matriz de ceros.
    # "for columna in range(columnas)" fila interna: genera cada elemento de la lista(genera 10 ceros). Seria como generar las cabezas de las columnas.
    # " for fila in range(filas)" fila externa: genera cada fila de la matriz(genera 10 filas).
    # "range()" genera los indices de cada columna dentro de una fila. Genera los indices de cada fila de la matriz.
    # Tambien con "range()" el programa sabe cuantas veces repetir el bucle de fila y columna para construir la matriz.   
    return [[0 for columna in range(columnas)] for fila in range(filas)]



# Definimos la funcion que pide al usuario el tamanho del mapa, numero de filas y columnas.
def pedir_tamanho_mapa():

# Definimos el tamanho por defecto del mapa inicial (10 filas, 10 columnas).
# df -> defecto.
    filasdf = 10
    columnasdf = 10    

    # Se usa "try" para manejar errores como mal ingreso de datos de parte del usuario y como reaccionar ante esos errores.
    # Es en el caso de que el usuario ingrese un dato que no sea el tamanho de filas y columnas.
    # Si el usuario escribe algo como “hola”, int() genera un error (ValueError).
    # En lugar de que el programa se detenga con un mensaje feo, se ejecuta el bloque except y muestra un aviso.
    try:
        user_filas = int(input("Ingrese el número de filas: "))
        user_columnas = int(input("Ingrese el número de columnas: "))
    
    # En "except" se pone el bloque de codigo que va a manejar el error.
    except ValueError:
        
        # Se imprime un mensaje en pantalla, si no ingresa números de filas  y columnas usamos el tamaño por defecto.
        print("Entrada inválida, debe de ingresar el numero de filas y columnas.")
        return filasdf, columnasdf

    # Condicional que controla el tamanho minimo del mapa(5x5) que ingrese el usuario.
    if user_filas < 5 or user_columnas < 5:
        
        # Imprimimos en pantalla un mensaje avisando al usuario el tamanho minimo requerido, y que se usara el tamanho por defecto.
        print("El tamanho minimo del mapa es de 5x5, se usara 10x10 por defecto.")
        # Devolvemos el valor de las filas y columnas por defecto que tiene que usar el programa.
        return filasdf, columnasdf

    # Retorna el valor de los datos ingresados por el usuario.(tamanhos de filas y columnas)
    return user_filas, user_columnas


#====================================FUNCION AUXILIAR DE COLOCAR OBSTACULOS FIJOS==========================================#

# Definimos una funcion auxiliar, que coloca los obstaculos en celdas vecinas. 
# Si la celda iniciamente en donde se queria poner el obstaculo esta ocupada.
def colocar_obst_celdasvecinas(mapa, fila_inicial, col_inicial,valor):
    
    # (0,0) posicion actual + 4 direcciones cardinales + 4 direcciones diagonales.
    # La funcion recorre estas coordenadas en orden, y coloca el obstaculo en la primera celda libre que encuentre.
    # Esto asegura que si la posicion inicial esta ocupada, el obstaculo siempre se colocoque en una celda vecina valida.
    vecinos = [(0,0), (1,0),(-1,0),(0,1),(0,-1), (1,1),(1,-1),(-1,1),(-1,-1)]

    # En este bucle for recorremos las posiciones vecinas para colocar los obstaculos en una celda libre.
    # "df" desplazamineto de fila, "dc" dezplazamiento de columna.
    # "ff" va a contener la fila candidata en la que se podria colocar el obstaculo.
    # "cc" va a contener la columna candidata en la que se podria colocar el obstaculo.
    for df, dc in vecinos:
        
        # Se calcula sumando el desplazamiento(df, dc) al indice original(fila_inicial,col_inicial).
        # "ff" y "cc" van contener las coordenas de fila y columna en donde se pondran los obstaculos.
        ff = fila_inicial + df
        cc = col_inicial + dc

        # Esta condicion garantiza que la celda candidata a contener el obstaculo, este dentro del rango y este libre antes de colocar el obstaculo.
        # "len(mapa)" devuelve el total de filas de la matriz, len(mapa[0]) devuelve el total de columnas de la primera fila.
        if 0 <= ff < len(mapa) and 0 <= cc < len(mapa[0]) and mapa[ff][cc] == 0:
            
        # "valor" contiene el numero que representa el tipo de obstaculo que vamos a colocar en la celda.
            mapa[ff][cc] = valor
        
        # Termina la funcion, porque ya se encontro una celda libre en donde colocar el obstaculo. 
            break



# Definimos la funcion que va a colocar los obstaculos de edificio y agua, que seran obstaculos que se adaptaran al tamanho del mapa.
# (mapa) usamos mapa como parametro de la funcion para hacer los cambios dentro del mapa para agregar los obstaculos. 
def colocar_obstaculos_fijos(mapa):
    
    # Este bloque de codigo asegura que la funcion sepa el tamanho del mapa.
    # "if mapa" comprueba que mapas tenga filas, "mapa[0]" comprueba que la primera fila tiene almenos una columna, para saber que haya columnas tambien en el mapa.
    if mapa and mapa[0]: 
        
        # Mide la longitud de la matriz, con estas dos lineas el programa sabe el tamanho de la matriz
        # "filas = len(mapa)" devuelve cuantas filas hay en la matriz. (cantidad total de filas)
        # "columnas = len(mapa[0])" cuenta cuantas columnas hay en esa fila. (cantidad de columnas en cada fila)
        filas = len(mapa)
        columnas = len(mapa[0])

    # Definimos en este bloque la cantidad de obstaculos que va a tener la matriz.(1 de edificios).
    # Calcula el total de filas x el total de columnas y el resultado lo multiplica por "0.2".(20%)
    # Para sacar el porcentaje de edificios que tendra el mapa.
    cantidad_edificios = int(filas * columnas * 0.2)
    

    # Recorre la cantidad de edificios que tenga "cantidad_edificios". 
    # "Edificio" toma el valor de cada edificio, solo se usa para contar las repeticiones, no se usa dentro del bloque.  
    for edificio in range(cantidad_edificios):

        # "random.randint" genera un numero aleatorio para la coordenada de fila y columna, dentro de la matriz(0, fila -1)
        # En cada iteracion se selecciona una celda (fila,columna) distinta al azar, tantas veces que contenga "cantidad_edificos "  
        fila_random = random.randint(0, filas-1)
        col_random = random.randint(0, columnas-1) 
    
    # Se llama a la funcion con parametros del mapa, la coordenada de fila, coordenada de columna, y el valor de edificio que es 1.
    # Si las celdas en donde inicialmente se querian poner los edificios estan ocuapdas esta funcion auxiliar se encarga de ponerles en un lugar.
        colocar_obst_celdasvecinas(mapa, fila_random,col_random, valor = 1)


# Definimos una funcion para realizar las calles del mapa con un patron repetido.
def generar_calles(mapa):

    # Iniciamos un bucle que recorre toda la matriz y en funcion del patron se decide si esa celda va a ser un camino libre.
    for fila in range(len(mapa)):
        for columna in range(len(mapa[0])):

            # Si la fila que se analiza al dividir por 3 su resto es 1, entonces esa celda su valor sera 0.
            # O si la columna que se analiza al dividir por 3 su resto sea 1, entonces esa celda su valor sera 0
            if fila % 3 == 1 or columna % 3 == 1:
                mapa[fila][columna] = 0

            # Y si su resto es cero entonces conserva el valor que tiene.
            else:
                mapa[fila][columna] = 1



# Definimos una funcion para que el usuario pueda colocar los obstaculos temporales que elija.
def colocar_obstaculo_temporal(mapa):

    # Este bloque devuelve el numero de filas y columnas de la matriz(mapa).
    filas = len(mapa)
    columnas = len(mapa[0])

    # Se inicia un bucle para pedir el tamanho de filas y columnas al usuario hasta que coloque los datos correctos.
    while True:
    
    # Se usa try para manejar los errores de datos mal ingresados por parte del usuario, lo usamos para el programa pueda manejar los errores.
    # En el caso de que el usuario ingrese un valor que no sea una coordenada de filas y columnas se ejecuta el bloque "except".
    # "except" en su bloque hay un mensaje que se imprime en la pantalla de la consola avisandole al usuario que tiene que ingresar coordenadas.
        try:
            
            # Pedimos al usuario el tipo de obstaculo que quiera ingresar y lo guardamos en la variable tipo_obstaculo.
            tipo_obstaculo = int(input("Ingrese 2 para agua o 3 para obstaculo temporal: "))

        # Vericamos que tipo de obstaculo ingreso el usuario, si ingreso un valor que no sea 2 o 3.
        # La funcion no la va reconocer y le imprimira un mensaje en pantalla indicandole que el tipo de obstaculo que ingreso es invalido.
        # "continue" hace un salto del resto del codigo restante, no ejecuta el resto del código de esa iteración. 
        # Esto evita errores y mantiene limpio el flujo de control. Se ejecuta cuando no se ingresa un valor valido para la funcion.
            if tipo_obstaculo not in [2,3]:
                print("Tipo de obstaculo invalido, solo puede ser 2 o 3.")
                continue
            
        # El bloque que maneja los errores de tipos de datos mal ingresados, se ejecuta este bloque y se muestra un mensaje en pantalla.
        # Se le indica al usuario que debe de ingresar valores enteros.
        except ValueError:
            print("Entrada invalida. Debe ingresar numeros enteros.")    
            
        # Usamos try para manejar errores que pueda cometer el usuario al ingresar mal los datos de coordenadas.
        try:

        # Pedimos al usuario que ingrese la coodenada de fila y columna en donde quiera colocar los obstaculos temporales    
            fila_usuario = int(input(f"Ingrese la fila (0 a {filas - 1}): "))
            col_usuario = int(input(f"Ingrese la columna (0 a {columnas - 1}): "))

        
        # Bloque de codigo que maneja los errores, al ingresar mal los datos necesarios para la funcion.
        # Se imprime un mensaje indicandole al usuario que debe ingresar coordenadas validas para la fila y columna.
        # "continue" hace un salto del resto del codigo restante, no ejecuta el resto del código de esa iteración. 
        # Esto evita errores y mantiene limpio el flujo de control. Se ejecuta cuando no se ingresa un valor valido para la funcion.
        except ValueError:
            print("Debe ingresar números válidos para fila y columna.")
            continue
        
        # Esta condicional verfica que la fila y columna igresada por el usuario este dentro del rango de la matriz.
        # Si no es asi, entonces imprime un mensaje en pantalla indicando que las coordenadas ingresadas estan fuera del rango del mapa.
        # "continue" hace un salto del resto del codigo restante, no ejecuta el resto del código de esa iteración. 
        # Esto evita errores y mantiene limpio el flujo de control. Se ejecuta cuando no se ingresa un valor valido para la funcion.
        if not (0 <= fila_usuario < filas) or not (0 <= col_usuario < columnas):
            print("Coordenadas fuera del rango del mapa")
            continue


        # Verificamos que si las coordenadas de fila y columna que ingreso el usuario no esten ocupadas.
        # Si estan ocupadas, se imprime un mensaje en pantalla indicando que la celda esta ocupada en esa posicion, y que elija otrra posicion.
        # "continue" hace un salto del resto del codigo restante, no ejecuta el resto del código de esa iteración. 
        # Esto evita errores y mantiene limpio el flujo de control. Se ejecuta cuando no se ingresa un valor valido para la funcion.
        # if mapa[fila_usuario][col_usuario] != 0:               
        #     print("La celda ya esta ocupada, elija otra.")
        #     continue
        
        # if mapa[fila_usuario][col_usuario] != 6:               
        #     print("La celda ya esta ocupada, elija otra.")
        #     continue

    
        # Se ingresa en el mapa la coordenada de fila y columna en donde se agregara el tipo de obstaculo ingresado.
        mapa[fila_usuario][col_usuario] = tipo_obstaculo
        print(f"Obstaculo de tipo {tipo_obstaculo} colocado en ({fila_usuario}, {col_usuario}).")

        # Preguntamos si quiere agregar mas obstaculos, si ya no quiere agregar obstaculos se rompe el bucle y termina la funcion.
        continuar = input("desea agregar otro obstaculo temporal? (s/n): ").lower()
        if continuar != 's' :
            break


# Funcion que le pide el usuario las coordenadas de inicio y el destino para colocarlos en el mapa.
def inicio_destino_user(mapa):

    # Este bloque devuelve el numero de filas y columnas de la matriz(mapa).
    filas = len(mapa)
    columnas = len(mapa[0])

    # Iniciamos un bucle que se va a repetir hasta que el usuario ingrese las coordenadas de inicio y destino correctamente.
    while True:

        try:

            # En este bloque de codigo se le pide al usuario ingresar las coordenadas de inicio y destino.
            fila_inicio = int(input(f"Ingrese la fila de inicio (0 a {filas -1}): "))
            columna_inicio = int(input(f"Ingrese la columna de inicio (0 a {columnas -1}): "))

            fila_destino = int(input(f"Ingrese la fila de destino (0 a {filas -1}): "))
            columna_destino = int(input(f"Ingrese la columna de destino (0 a {columnas -1}): "))


        # Bloque de codigo que maneja errores, en el caso que el usuario no ingrese numeros para las coordenadas.
        except ValueError:
            print("Ingrese numeros enteros")
            continue


        # Verifica si las coordenadas de inicio que el usuario ingreso estan dentro del rango del mapa.
        if not (0 <= fila_inicio < filas) or not (0 <= columna_inicio < columnas):
            print("Coordenadas de inicio fuera del mapa.")
            continue

        # Verifica si las coordenadas de destino que el usuario ingreso estan dentro del rango del mapa.    
        if not (0 <= fila_destino < filas) or not (0 <= columna_destino < columnas):
            print("Coordenadas de destino fuera del mapa.")
            continue


        # Verifica que las celda de inicio que ingreso el usuario este libre (0 = calle)
        if mapa[fila_inicio][columna_inicio] != 0:
            print("La celda de inicio esta ocupada, elija otra celda.")
            continue

        # Verifica que las celda de destino que ingreso el usuario este libre (0 = calle)
        if mapa[fila_destino][columna_destino] != 0:
            print("La celda de destino esta ocupada, elija otra celda.")
            continue
        
        # Coloca valor de inicio y destino en el mapa usando (inicio = 4, destino = 5)
        mapa[fila_inicio][columna_inicio] = 4
        mapa[fila_destino][columna_destino] = 5

        # Se imprime un mensaje en pantalla indicando las coordenadas de inicio y destino al usuario.
        print(f"Inicio colocado en ({fila_inicio}, {columna_inicio})")
        print(f"Destino colocado en ({fila_destino}, {columna_destino})")

    # Retorna las coordenadas de inicio y destino al programa.
        return(fila_inicio, columna_inicio), (fila_destino, columna_destino)
    

# Definimos la funcion heuristica (Manhattan) que calcula la distancia heuristica entre nodos.
def heuristica(a,b):

    # "a y b" son tuplas (fila, columna)
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) 

# definimos la funcion del algorimo A* que va a econtrar la ruta mas optima y con menor costo hasta el destino que el usuario elija.
def a_estrella(mapa, inicio, destino):
    
    # Definimos un diccionario con los costos según el tipo de celda
    costo_terreno = {
        0: 1,        # Camino/calle libre
        1: float('inf'),  # Edificio (no se puede pasar)
        2: 3,        # Agua
        3: float('inf'),        # Obstáculo temporal
        4: 1,        # Inicio
        5: 1,        # Destino
        6: 1         # Ruta marcada (si quieres usarlo)
    }


    # Esta variable contiene los posibles movimientos que se pueden hace en el programa.
    # Cada tupla (df, dc) indica como cambiar de fila y columna para ir a una celda vecina.
    movimientos = [(-1,0),(1,0),(0,-1),(0,1)]


    # Esta variable contiene una lista que se usara como cola de prioridad (implementada con heapq).
    # Cada elemento es una tupla (f, coordenadas) "donde f = g + h es el costo estimado".
    # Inicialmente solo tiene el punto de inicio con costo cero.
    cola_prioridad = [(0, inicio)]
    
    # Este diccionario va a guardar las coordenadas anteriores de cada celda para reconstuir el camino con la solucion.
    procedencia = {}

    # Esta variable va a guardar el costo real, desde el inicio hasta cada celda.
    # inicio : 0 porque al empezar, el costo de llegar al inicio es 0.
    costo_g = {inicio: 0}

    # Este while lo que hace es mantener el bucle activo mientras cola_prioridad tenga elementos.
    # Mientras la lista de cola prioridad tenga elementos, seguimos en el bucle. (Una lista vacia se considera False).
    # Si la cola se vacía, significa que ya no hay más caminos posibles y el bucle termina.
    while cola_prioridad:

        # "heapq.heappop(cola_prioridad)" Saca el nodo con menor costo de la cola de prioridad.
        # Lo separa en dos variables: "costo_f" (el costo total) y "actual" (la posición en el mapa).
        # El nodo se elimina de la cola, evitando que se repita el procesamiento.
        costo_f, actual = heapq.heappop(cola_prioridad)

        # Verificamos si la celda actual es el destino.
        # Si lo es, hemos llegado y se procede a reconstruir el camino desde el destino hasta el inicio.
        # Si no, el algoritmo sigue explorando otras celdas.
        if actual == destino:

            # Creamos la lista "camino" e inicializamos con la coordenada de destino.
            # A partir de aquí se irán agregando las celdas anteriores hasta llegar al inicio.
            camino = [destino]

            # Mientras la celda actual tenga un "padre" en el diccionario procedencia,
            # seguimos retrocediendo desde el destino hasta el inicio.
            # "procedencia" guarda de qué celda venía cada coordenada, permitiendo reconstruir la ruta.
            while actual in procedencia:

                # En esta linea se hace el retroceso de un paso en el camino.
                # "actual" se actualiza con la celda "padre" desde la que llegó.
                actual = procedencia[actual]

                # Agregamos la coordenada actual al final de la lista "camino".
                # Como estamos retrocediendo desde el destino, la lista queda en orden inverso (destino → inicio).
                # La lista "camino" se va llenando en orden inverso: primero el destino, luego su padre
                camino.append(actual)

                # Invertimos la lista "camino" para que quede en orden inicio → destino.
                # [::-1] significa recorrer la lista desde el final hacia el principio.
                # : → desde el inicio hasta el final. -1 → con un paso negativo, recorriendo de atrás hacia adelante.
                # De esta manera el resultado ya puede usarse paso a paso en el orden correcto.
                # "return" la devuelve ya lista para ser usada por el algoritmo.
            return camino[::-1] 


        # Este bloque de codigo se usa para que A* recorra las celdas vecinas a la celda actual y verifica si es una celda valida
        # En la que pueda moverse( dentro del mapa, que sea libre, o sea el destino)
        for df, dc in movimientos:

            # Calcula la coordenada del vecino sumando el cambio de fila (df) y columna (dc) a la posicion actual.
            vecino = (actual[0] + df, actual[1] + dc)

            # Validar dentro del mapa y que sea transitable
            # Se asegura que la coordenada del vecino esté dentro del rango de la matriz.
            # Se descartan automáticamente las celdas que no se pueden atravesar (edificios, costo = inf).
            # Si la celda es transitable, se agrega a la cola de prioridad como un movimiento válido.
            # Más tarde, cuando esa celda salga de la cola, el algoritmo seguirá explorando y construyendo el camino.
            if (0 <= vecino[0] < len(mapa) and
                0 <= vecino[1] < len(mapa[0]) and
                costo_terreno[mapa[vecino[0]][vecino[1]]] != float('inf')):


            # Este bloque es el corazon de A* su finalidad es calcular cuanto costaria llegar al vecino por la ruta que acaba de explorar el programa.
            # Y si se encuentra una ruta mejor que lo que ya se tenia, se guarda y agrega a la cola de prioridad para procesarla.
                
                # Obtenemos el tipo de terreno de la celda vecina
                tipo_vecino = mapa[vecino[0]][vecino[1]]

                # Calculamos el costo según el terreno
                nuevo_costo_g = costo_g[actual] + costo_terreno[tipo_vecino]
                
                # Se verifica si la celda vecina aún no tiene un costo registrado o si se encontró un costo menor para llegar a ella.
                # Si la celda no tiene costo, significa que aún no se exploró y se registra ahora en costo_g.
                # Si el nuevo costo es menor al registrado, se actualiza para reflejar la ruta más corta encontrada hasta el momento.
                # Si ninguna de estas condiciones se cumple, no se actualiza nada porque la ruta actual no es mejor.
                # Esto garantiza que A* siempre conserve la ruta de menor costo acumulado desde el inicio.
                if vecino not in costo_g or nuevo_costo_g < costo_g[vecino]:
                    
                    # Aquí se guarda el costo acumulado más bajo encontrado hasta llegar a la celda vecina.
                    # Este valor representa el costo real (g) desde el inicio hasta esta celda.
                    # Se usará tanto para comparar futuros caminos a esta celda como para reconstruir la ruta óptima al final.
                    costo_g[vecino] = nuevo_costo_g
                    
                    # Aquí se calcula el valor de prioridad "f = g + h" para la celda vecina.
                    # g = costo acumulado desde el inicio hasta esta celda (nuevo_costo_g)
                    # h = estimación heurística de la distancia desde la celda vecina hasta el destino (heuristica)
                    # f representa el costo total estimado de llegar al destino pasando por esta celda.
                    # Este valor se usará para decidir qué celda explorar primero en la cola de prioridad.
                    f = nuevo_costo_g + heuristica(vecino, destino)
                    
                    # Se agrega el vecino en la cola_prioridad (heap) con su costo total f.
                    # La función heapq.heappush mantiene la estructura de heap,
                    # asegurando que la celda con menor f (prioridad más alta) esté siempre al frente.
                    # A* procesará primero los nodos con menor f, explorando caminos más prometedores primero.
                    heapq.heappush(cola_prioridad, (f, vecino))
                    
                    # Se guarda la coordenada de procedencia de la celda vecina.
                    # Esto indica que para llegar a 'vecino' se vino desde 'actual'.
                    # Se usará más tarde para reconstruir el camino desde destino hasta inicio.
                    procedencia[vecino] = actual

    # Se devuelve None si no se pudo encontrar un camino hacia el destino.
    # Esto sucede cuando todas las celdas posibles se exploraron y no hay ruta disponible.
    return None  

# Definimos la funcion para imprimir la matriz con los emojis correspondientes a su valor en la matriz.
def imprimir_mapa(mapa):

    # Diccionario para darle a cada valor un caracter que lo represente.
    emojis = {
        0: "⬛",
        1: "🏢",
        2: "🔵",
        3: "🚧",
        4: "🚘",
        5: "🏁",
        6: "🟢"
    }

    # Este bucle recorre cada celda de la fila y reemplaza cada valor con su emoji correspondiente.
    for fila in mapa:

        # " ' '.join( )" une los emojis con espacios para que la matriz sea agradable a la vista sin puntos.
        # "emojis.get" busca en el diccionario "emojis" el emoji que corresponde a cada valor en las celdas.
        # Si no encuentra el emoji para un valor en el mapa usa "❓" para representarlo.
        # "for celda in fila" recorre cada elemento de la lista "fila"
        linea = ' '.join(emojis.get(celda, "❓") for celda in fila)
        print(linea)
    print()

# ---------------- PROGRAMA PRINCIPAL CON MENU ---------------- #

# Este bloque de codigo inicializa la matriz con calles, edificios y el tamanho de mapa que elija el usuario.

# Se llama a la funcion para pedir el tamanho del mapa al usuario, user_filas, user_columnas guarda esos valores.
# No tiene sentido usar parametros en este caso porque la idea es que el usuario elija el tamanho del mapa.
# Si quisieramos tener una tamanho fijo se usaria parametros en vez de variables con los valores que ingreso el usuario.
user_filas, user_columnas = pedir_tamanho_mapa()

# Se llama a la funcion para generar la matriz inicial de enteros.
mapa = generar_matriz(user_filas, user_columnas)

# Se llama a la funcion para colocar los osbtaculos fijos de la matriz. 
colocar_obstaculos_fijos(mapa)

# Se llama a la funcion que genera las calles de la matriz
generar_calles(mapa)

# Se inicializa las variables (inicio, destino, camnino) sin ningun valor, se inicializan con None, porque el usuario los definira despues.
inicio = None
destino = None
camino = None

while True:
    print("\n--- MENU ---")
    print("1) Mostrar mapa")
    print("2) Agregar obstáculo temporal")
    print("3) Colocar inicio y destino")
    print("4) Resolver camino con A*")
    print("5) Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        imprimir_mapa(mapa)
        
    elif opcion == "2":
        colocar_obstaculo_temporal(mapa)
        imprimir_mapa(mapa)
    
    elif opcion == "3":
        inicio, destino = inicio_destino_user(mapa)
        
    elif opcion == "4":
        if inicio is None or destino is None:
            print("Primero colocá inicio y destino (opción 3).")
            continue
        
        # Se llama a la funcion para buscar la ruta mas corta con menor costo, desde el inicio hasta el destino que el usuario defina.
        camino = a_estrella(mapa, inicio, destino)
        
        # Verfica si camino contiene un camino o si no contine nada(None). Si contiene las coordenadas hasta el destino entra en el bloque de codigo for.
        # Si no contiene nada, salta al bloque else. 
        if camino:
            
            # Recorre cada posicion (fila, columna) que forma parte de la ruta.
            for f, c in camino:

                # Se asegura de no marcar la celdas de inicio y destino.
                if mapa[f][c] == 0:

                    # Asigna el valor de 6 a las celdas libres(0) marcando la ruta de inicio hasta el destino.  
                    mapa[f][c] = 6

            # Muestra en pantalla el mapa con el camino marcado.         
            imprimir_mapa(mapa)
        else:
            print("No se encontró un camino disponible.")
    
    elif opcion == "5":
        print("Saliendo...")
        break
    
    else:
        print("Opción inválida, elige nuevamente.")

