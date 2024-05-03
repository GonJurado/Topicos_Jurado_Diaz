import matplotlib.pyplot as plt
import numpy as np

def draw_custom_beehive_hex_grid():
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    
    hex_size = 1.0
    angle = 2 * np.pi / 6
    total_hexagons = 37
    side_length = 4

    # Coordenadas del centro del tablero
    center_x = 0
    center_y = 0

    # Lista para almacenar las coordenadas de los hexágonos
    hex_coords = []

    # Crear los hexágonos en cada fila según la disposición específica
    num_hexagons = [4, 5, 6, 7, 6, 5, 4]

    for row, num in enumerate(num_hexagons):
        start_x = center_x - (num - 1) * 3 / 2 * hex_size
        start_y = center_y + (3 * row - 6) * np.sqrt(3) / 2 * hex_size
        
        for i in range(num):
            x = start_x + i * 3 * hex_size
            y = start_y
            hex_coords.append((x, y))

    # Dibujar los hexágonos
    for coord in hex_coords:
        x, y = coord
        vertices = []
        for j in range(6):
            vertices.append((x + hex_size * np.cos(j * angle),
                             y + hex_size * np.sin(j * angle)))
        ax.add_patch(plt.Polygon(vertices, edgecolor='black', lw=2, fill=False))

    ax.autoscale_view()
    ax.axis('off')
    plt.show()

draw_custom_beehive_hex_grid()
