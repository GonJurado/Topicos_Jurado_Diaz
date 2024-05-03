import random
import tkinter as tk
from ortools.sat.python import cp_model

def crearCamino(size):
    path = []
    conectores = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    actual = (random.randint(0, size-1), random.randint(0, size-1))
    path.append(actual)
    used = set(path)

    while len(path) < size * size:
        acciones = [(actual[0] + dx, actual[1] + dy) for dx, dy in conectores
                          if 0 <= actual[0] + dx < size and 0 <= actual[1] + dy < size
                          and (actual[0] + dx, actual[1] + dy) not in used]
        if not acciones:
            path, used = [], set()
            actual = (random.randint(0, size-1), random.randint(0, size-1))
            path.append(actual)
            used.add(actual)
        else:
            actual = random.choice(acciones)
            path.append(actual)
            used.add(actual)
    return path

def resolverRikudo(size, path, canvas):
    model = cp_model.CpModel()

    # Creamos numeros de 1-n**2 para la tabla
    tabla = {}
    for i, pos in enumerate(path):
        tabla[pos] = model.NewIntVar(1, size * size, f'cell_{pos}')

    # Validar que el camino esté bien
    for i in range(1, len(path)):
        model.Add(tabla[path[i]] == tabla[path[i-1]] + 1)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        solucionTabla = [[0] * size for _ in range(size)]
        for pos, var in tabla.items():
            solucionTabla[pos[0]][pos[1]] = solver.Value(var)
            actualizar(canvas, solucionTabla)
            canvas.update()
        return solucionTabla
    else:
        return None

def actualizar(canvas, solucionTabla):
    canvas.delete("all")
    for i in range(len(solucionTabla)):
        for j in range(len(solucionTabla[i])):
            canvas.create_text(j * 30 + 15, i * 30 + 15, text=str(solucionTabla[i][j]))

def solucionar():
    size = int(entry.get())
    ruta = crearCamino(size)

    root = tk.Toplevel()
    root.title("Rikudo Solucionador")

    canvas = tk.Canvas(root, width=size * 30, height=size * 30, bg="white")
    canvas.pack()

    solution = resolverRikudo(size, ruta, canvas)

    if solution:
        print("Solucion hallada:")
        for row in solution:
            print(' '.join(f"{val:2d}" for val in row))
    else:
        print("No se encontro una solucion.")

def main():
    global entry
    root = tk.Tk()
    root.title("Rikudo Solucionador")

    label = tk.Label(root, text="Ingresar el tamaño del tablero:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    solve_button = tk.Button(root, text="Resolver", command=solucionar)
    solve_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
