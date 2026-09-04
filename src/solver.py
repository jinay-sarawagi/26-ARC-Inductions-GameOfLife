def count_neighbors(grid, row, col):
    alive_count = 0

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Check all 8 surrounding cells
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:

            # Skip the cell itself
            if dr == 0 and dc == 0:
                continue

            new_row = row + dr
            new_col = col + dc

            # Make sure the neighbor is inside the grid
            if 0 <= new_row < rows and 0 <= new_col < cols:
                alive_count += grid[new_row][new_col]

    return alive_count


#---------------------------- TASK 2 ----------------------------
def compute_next_generation(grid):
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # Create a new blank grid
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    # Check every cell
    for row in range(rows):
        for col in range(cols):

            # Count its alive neighbors
            neighbors = count_neighbors(grid, row, col)

            # Rule 1, 2 and 3:
            # A live cell survives only with 2 or 3 neighbors
            if grid[row][col] == 1:
                if neighbors == 2 or neighbors == 3:
                    next_grid[row][col] = 1
                else:
                    next_grid[row][col] = 0

            # Rule 4:
            # A dead cell becomes alive with exactly 3 neighbors
            else:
                if neighbors == 3:
                    next_grid[row][col] = 1
                else:
                    next_grid[row][col] = 0

    return next_grid
