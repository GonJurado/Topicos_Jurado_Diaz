# Informe TP: Resolución de Tablero Rikudo

## Introducción

El juego de rompecabezas Rikudo, basado en un personaje del anime Naruto, fue creado en el año 2015. El objetivo del juego es colocar las piezas en un tablero de 36 casillas de tal manera que se cumplan ciertas restricciones. Este informe describe la implementación de un programa para resolver el problema de Rikudo utilizando técnicas de Programación por Restricciones (CSP).

## Motivación

Los juegos de rompecabezas son una forma divertida y desafiante de ejercitar la mente. Rikudo, en particular, ofrece un nivel de complejidad que lo hace atractivo para jugadores experimentados. Además, la aplicación de técnicas de inteligencia artificial para resolver este tipo de problemas puede tener aplicaciones prácticas en otras áreas, como la planificación y la optimización.

## Técnica Propuesta

La técnica propuesta para resolver el problema de Rikudo es la de Programación por Restricciones (CSP). Esta técnica se basa en la definición de un conjunto de variables, un conjunto de dominios para cada variable y un conjunto de restricciones que deben satisfacerse para encontrar una solución válida. En el caso de Rikudo, las variables serían las casillas del tablero, los dominios serían las piezas que pueden colocarse en cada casilla y las restricciones serían las reglas del juego.

## Objetivos

Los objetivos del proyecto son los siguientes:

- Modelar el problema de Rikudo como un CSP.
- Resolver el problema de Rikudo utilizando un solver de CSP.
- Implementar una interfaz gráfica para resolver cualquier tablero de Rikudo de tamaño 36.

## Marco Teórico

- Programación por Restricciones (CP):
  Este paradigma se utiliza para la programación enfocada en la resolución de problemas. Para encontrar una solución, se definen restricciones o limitaciones que reducen el rango de resultados a aquellos capaces de cumplir las necesidades del problema. CP se separa por dos tipos de problemas, optimización y satisfacción, de los cuales este caso se diseñará en base a satisfacción (CSP), la búsqueda de cualquier solución al problema que cumpla con las reglas establecidas.

- Reglas de Rikudo:
  En base a las reglas del juego Rikudo, se definen ciertas restricciones y limitaciones al CSP del programa. El problema solo puede tener 36 números i, los cuales cada uno necesita ser conectado por sus valores vecinos (i - 1 → i → i + 1). Para ello, la solución debe utilizar un tablero hexagonal con n valores iniciales y llenar cada punto con un valor único entre 1 y 36 de tal manera que haya una línea continua entre todos los puntos y que no deje ningún punto vacío.

- Librerías de CP:
  Considerando que se utilizará como lenguaje de programación a Python, se pueden utilizar librerías como Ortools para la definición de un solucionador con reglas al igual que PySide para el diseño de la interfaz gráfica.

- Interfaz Gráfica (GUI):
  Cuando se haya definido la solución, el programa debe devolver una interfaz gráfica que muestre el tablero inicial que sea reemplazado al presionar un botón por el tablero solucionado.

## Desarrollo

Implementación del Código
El código del programa se ha implementado utilizando las siguientes librerías:

- random para generar un camino aleatorio en el tablero.
- tkinter para crear la interfaz gráfica del usuario.
- ortools.sat.python para definir y resolver el problema de CSP.

El código se divide en las siguientes funciones:

1. crearCamino(size): Genera un camino aleatorio en un tablero de tamaño size.
2. resolverRikudo(size, path, canvas): Resuelve el problema de Rikudo para un tablero de tamaño size y un camino inicial path. La solución se muestra en un canvas.
3. actualizar(canvas, solucionTabla): Actualiza el canvas con la solución del problema.
4. solucionar(): Obtiene el tamaño del tablero del usuario, genera un camino aleatorio y resuelve el problema.
5. main(): Crea la interfaz gráfica del usuario y ejecuta la función solve_puzzle().

## Interfaz Gráfica

La interfaz gráfica del usuario consiste en una ventana con una entrada de texto para ingresar el tamaño del tablero y un botón para resolver el problema. Al presionar el botón, el programa genera un camino aleatorio en el tablero y resuelve el problema. La solución se muestra en una nueva ventana con el tablero completo.

## Conclusiones

- El programa implementado es capaz de resolver el problema de Rikudo para tableros de cualquier tamaño. 
- La interfaz gráfica del usuario permite a los usuarios ingresar el tamaño del tablero y ver la solución del problema.
- Se ha demostrado que la técnica de Programación por Restricciones es una herramienta efectiva para resolver este tipo de problemas de rompecabezas.

## Referencias
- Rikudo-puzzle.com - Free Rikudo puzzles online. (s. f.). Rikudo. Recuperado de:<br>
  https://www.rikudo-puzzle.com/
- Python reference: CP-SAT. (s. f.). Google For Developers. Recuperado de:<br>
  https://developers.google.com/optimization/reference/python/sat/python/cp_model
