🗺️ Proyecto 3: City Pathfinding - Algoritmo A* & Heurística Manhattan

Este proyecto es un simulador de navegación urbana en consola que genera un mapa de ciudad con edificios, calles y obstáculos, encontrando la ruta más óptima entre dos puntos utilizando Inteligencia Artificial.

📖 Descripción

El programa genera una cuadrícula representativa de una ciudad donde el usuario puede definir el tamaño, colocar obstáculos temporales (como obras o inundaciones) y establecer un punto de inicio y destino. El sistema calcula la ruta más corta evitando colisiones y visualizando el resultado con una interfaz amigable de emojis.

🛠️ Tecnologías Utilizadas

Lenguaje: Python 3
Algoritmos de IA: A* (A-Star) con Heurística de Manhattan.
Estructuras de Datos: heapq (Binary Heap / Priority Queue) para optimización de búsqueda, Diccionarios y Listas por comprensión.

🧠 Lógica y Algoritmos (Paso a Paso)

Este proyecto es un ejemplo claro de eficiencia algorítmica:

Algoritmo A*:

A diferencia de BFS, A* utiliza una función de costo $f(n) = g(n) + h(n)$.

g(n): El costo real acumulado desde el inicio.

h(n): La Heurística de Manhattan, que estima la distancia restante al destino.

Esto permite que el algoritmo "sepa" en qué dirección es más probable que esté la meta, ahorrando recursos computacionales.

Generación de Mapa Procedural:

Las calles se generan automáticamente usando lógica matemática (operador módulo %), creando un patrón de rejilla urbana.

Los edificios se colocan aleatoriamente asegurando una densidad del 20% del mapa.

Robustez y Manejo de Errores:

Implementación de bloques try-except para validar las coordenadas del usuario, evitando que el programa falle por entradas inválidas.

Cola de Prioridad (heapq):

Se utiliza para procesar siempre el nodo con el costo $f$ más bajo, garantizando que el camino encontrado sea el óptimo en el menor tiempo posible.

🚀 Cómo Ejecutarlo

Ejecuta el script:

Bash

python city_pathfinder.py

Define el tamaño del mapa (mínimo 5x5).

Usa el menú para agregar obstáculos (🔵 Agua o 🚧 Construcción).

Elige los puntos de inicio (🚘) y destino (🏁) para ver la magia de A*.
