# 🗺️ Proyecto: City Pathfinding — Algoritmo A* & Heurística Manhattan

Este proyecto es un **simulador de navegación urbana** en consola. Genera un mapa de ciudad con edificios, calles y obstáculos dinámicos, encontrando la ruta más óptima entre dos puntos utilizando Inteligencia Artificial avanzada.

## 📖 Descripción

El sistema genera una cuadrícula representativa de una ciudad donde el usuario tiene control total:
* **Personalización:** Definición del tamaño del mapa.
* **Dinamicidad:** Colocación de obstáculos temporales como obras (**🚧**) o inundaciones (**🔵**).
* **Visualización:** Interfaz amigable basada en emojis para representar el entorno y la ruta final.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.x
* **Algoritmos de IA:** A* (A-Star) con Heurística de Manhattan.
* **Estructuras de Datos:** * `heapq` (Binary Heap / Priority Queue) para optimizar la selección de nodos.
    * Diccionarios para el rastreo de costos y padres.
    * Listas por comprensión para un código más Pythonic y eficiente.

---

## 🧠 Lógica y Algoritmos

Este proyecto es un ejemplo claro de **eficiencia algorítmica** aplicada a problemas de optimización:

### 1. El Algoritmo A* (A-Star)
A diferencia de otros algoritmos de búsqueda, A* es "inteligente" porque utiliza una función de costo para priorizar el camino:
$$f(n) = g(n) + h(n)$$

* **$g(n)$**: El costo real acumulado desde el punto de inicio.
* **$h(n)$**: La **Heurística de Manhattan**, que estima la distancia restante al destino ignorando obstáculos.



Esta combinación permite que el algoritmo "sepa" en qué dirección es más probable que esté la meta, ahorrando recursos computacionales masivos en comparación con una búsqueda a ciegas.

### 2. Generación Procedural de Ciudad
* **Malla Urbana:** Las calles se generan automáticamente usando el **operador módulo (%)**, creando un patrón de rejilla realista.
* **Densidad de Edificios:** Se colocan obstáculos aleatorios asegurando una densidad del 20%, lo que garantiza que el mapa no esté ni demasiado vacío ni bloqueado por completo.

### 3. Optimización con Priority Queue (`heapq`)
Para garantizar que el sistema siempre procese el nodo con el costo $f$ más bajo, se implementó una **Cola de Prioridad**. Esto reduce la complejidad de búsqueda de $O(N)$ a $O(\log N)$, haciendo que el simulador sea rápido incluso en mapas grandes.

---

## 🚀 Cómo Ejecutarlo

1.  **Ejecuta el script principal:**
    ```bash
    python "nombredelarchivo".py
    ```
2.  **Configura el entorno:** Define el tamaño del mapa (mínimo 5x5).
3.  **Añade Desafíos:** Usa el menú para colocar agua o construcciones en el mapa.
4.  **Calcula la Ruta:** Define el punto de inicio (**🚘**) y el destino (**🏁**) para visualizar la ruta óptima calculada por la IA.

---
