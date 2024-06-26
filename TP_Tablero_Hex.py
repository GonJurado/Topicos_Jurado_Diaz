import matplotlib.pyplot as plt
import numpy as np

def dibujaTablaHex(tabla):
    _, ax = plt.subplots()
    ax.set_aspect('equal')
    
    hex_size = 1.0
    angle = 2 * np.pi / 6

    center_x = 0
    center_y = 0
    hex_coords = []
    hexagonos = [4, 5, 6, 7, 6, 5, 4]

    for row, num in enumerate(hexagonos):
        start_x = center_x - (num - 1) * 3 / 2 * hex_size
        start_y = center_y + (3 * row - 6) * np.sqrt(3) / 2 * hex_size
        
        for i in range(num):
            x = start_x + i * 3 * hex_size
            y = start_y
            hex_coords.append((x, y))

    # Dibujar los hexágonos con los valores del tablero
    for i, coord in enumerate(hex_coords):
        x, y = coord
        vertices = []
        for j in range(6):
            vertices.append((x + hex_size * np.cos(j * angle),
                             y + hex_size * np.sin(j * angle)))
        ax.add_patch(plt.Polygon(vertices, edgecolor='black', lw=2, fill=False))
        
        # Mostrar el valor del tablero dentro del hexágono
        if tabla[i] != "":
            ax.text(x, y, str(tabla[i]), ha='center', va='center', fontsize=12)

    ax.autoscale_view()
    ax.axis('off')
    plt.show()

# Definicion del tablero
tabla = [
    "", 30, 31, 32, 34, 36,
    2, 3, 29, 24, 33, 35,
    4, 6, 28, 25, 23, 21,
    7, 5, 26, 27, 22, 20,
    8, 9, 13, 14, 16, 19,
    10, 11, 12, 15, 17, 18,
    ""
]

dibujaTablaHex(tabla)