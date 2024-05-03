import random
import tkinter as tk
from ortools.sat.python import cp_model

def generate_valid_path(size):
    path = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    current = (random.randint(0, size-1), random.randint(0, size-1))
    path.append(current)
    used = set(path)

    while len(path) < size * size:
        possible_moves = [(current[0] + dx, current[1] + dy) for dx, dy in directions
                          if 0 <= current[0] + dx < size and 0 <= current[1] + dy < size
                          and (current[0] + dx, current[1] + dy) not in used]
        if not possible_moves:
            path, used = [], set()
            current = (random.randint(0, size-1), random.randint(0, size-1))
            path.append(current)
            used.add(current)
        else:
            current = random.choice(possible_moves)
            path.append(current)
            used.add(current)
    return path

def solve_rikudo_puzzle(size, path, canvas):
    model = cp_model.CpModel()

    # Create variables for each grid position
    grid = {}
    for i, pos in enumerate(path):
        grid[pos] = model.NewIntVar(1, size * size, f'cell_{pos}')

    # Ensure the sequence is correct
    for i in range(1, len(path)):
        model.Add(grid[path[i]] == grid[path[i-1]] + 1)

    # Create a solver and solve the model
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        solution_grid = [[0] * size for _ in range(size)]
        for pos, var in grid.items():
            solution_grid[pos[0]][pos[1]] = solver.Value(var)
            update_canvas(canvas, solution_grid)
            canvas.update()
        return solution_grid
    else:
        return None

def update_canvas(canvas, solution_grid):
    canvas.delete("all")
    for i in range(len(solution_grid)):
        for j in range(len(solution_grid[i])):
            canvas.create_text(j * 30 + 15, i * 30 + 15, text=str(solution_grid[i][j]))

def solve_puzzle():
    size = int(entry.get())
    random_path = generate_valid_path(size)

    root = tk.Toplevel()
    root.title("Rikudo Puzzle Solver")

    canvas = tk.Canvas(root, width=size * 30, height=size * 30, bg="white")
    canvas.pack()

    solution = solve_rikudo_puzzle(size, random_path, canvas)

    if solution:
        print("Solution found:")
        for row in solution:
            print(' '.join(f"{val:2d}" for val in row))
    else:
        print("No solution found.")

def main():
    global entry
    root = tk.Tk()
    root.title("Rikudo Puzzle Solver")

    label = tk.Label(root, text="Enter grid size:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    solve_button = tk.Button(root, text="Solve", command=solve_puzzle)
    solve_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
