from flask import Flask, jsonify, render_template
import random
import time
import threading
import numpy as np

app = Flask(__name__)

GRID_SIZE = 5  
level = 1
solving = False
solution_steps = []
original_grid = None  # Stores the initial state of the level

def create_solvable_grid(grid_size):
    """Creates a solvable Lights Out grid."""
    grid = [[0] * grid_size for _ in range(grid_size)]
    for _ in range(random.randint(grid_size, grid_size * 2)):  
        row, col = random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)
        toggle_light(grid, row, col, grid_size)
    return grid

def toggle_light(grid, row, col, size):
    """Toggles the clicked light and its adjacent ones."""
    grid[row][col] ^= 1
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = row + dr, col + dc
        if 0 <= nr < size and 0 <= nc < size:
            grid[nr][nc] ^= 1

def create_toggle_matrix(size):
    """Creates the toggle effect matrix for solving Lights Out."""
    n = size * size  
    A = np.zeros((n, n), dtype=int)

    for row in range(size):
        for col in range(size):
            index = row * size + col
            A[index, index] = 1  

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  
                nr, nc = row + dr, col + dc
                if 0 <= nr < size and 0 <= nc < size:
                    neighbor_index = nr * size + nc
                    A[index, neighbor_index] = 1  

    return A % 2  

def solve_lights_out(grid):
    """Solves the Lights Out puzzle using Gaussian elimination mod 2."""
    size = len(grid)
    A = create_toggle_matrix(size)
    b = np.array(grid).flatten()

    A_mod2 = A.copy()
    b_mod2 = b.copy()

    for i in range(len(A_mod2)):
        pivot = np.where(A_mod2[i:, i] == 1)[0]
        if len(pivot) == 0:
            continue  
        pivot = pivot[0] + i

        A_mod2[[i, pivot]] = A_mod2[[pivot, i]]
        b_mod2[[i, pivot]] = b_mod2[[pivot, i]]

        for j in range(i + 1, len(A_mod2)):
            if A_mod2[j, i] == 1:
                A_mod2[j] ^= A_mod2[i]  
                b_mod2[j] ^= b_mod2[i]

    x = np.zeros(len(A_mod2), dtype=int)
    for i in range(len(A_mod2) - 1, -1, -1):
        if A_mod2[i, i] == 1:
            x[i] = b_mod2[i] ^ np.dot(A_mod2[i, i + 1:], x[i + 1:]) % 2

    solution_moves = [(i // size, i % size) for i in range(len(x)) if x[i] == 1]
    return solution_moves

grid = create_solvable_grid(GRID_SIZE)
original_grid = [row[:] for row in grid]  # Save the initial grid state

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_grid")
def get_grid():
    return jsonify({"grid": grid, "level": level, "grid_size": GRID_SIZE, "solving": solving})

@app.route("/toggle/<int:row>/<int:col>")
def toggle(row, col):
    global grid
    toggle_light(grid, row, col, GRID_SIZE)
    return jsonify({"grid": grid, "level": level, "grid_size": GRID_SIZE})

@app.route("/reset_level")
def reset_level():
    """Resets the level to its original state."""
    global grid, original_grid, solution_steps
    grid = [row[:] for row in original_grid]  # Restore the saved grid
    solution_steps = []  # Clear solution when resetting
    return jsonify({"grid": grid, "level": level, "grid_size": GRID_SIZE, "solution_cleared": True})

@app.route("/reset_game")
def reset_game():
    """Resets the game to level 1 with a new grid."""
    global grid, level, original_grid, solution_steps
    level = 1
    grid = create_solvable_grid(GRID_SIZE)
    original_grid = [row[:] for row in grid]  # Save new level's grid state
    solution_steps = []
    return jsonify({"grid": grid, "level": level, "grid_size": GRID_SIZE, "solution_cleared": True})

@app.route("/next_level")
def next_level():
    """Progress to the next level with a new grid."""
    global grid, level, original_grid, solution_steps
    level += 1
    grid = create_solvable_grid(GRID_SIZE)
    original_grid = [row[:] for row in grid]  # Save new level's grid state
    solution_steps = []
    return jsonify({"grid": grid, "level": level, "grid_size": GRID_SIZE, "solution_cleared": True})

@app.route("/solve")
def solve():
    """Solves the puzzle based on the current grid state."""
    global solving, solution_steps
    solving = True
    solution_steps = solve_lights_out(grid)  # Always solve for the latest grid

    return jsonify({"steps": solution_steps})

if __name__ == "__main__":
    app.run(debug=True)
