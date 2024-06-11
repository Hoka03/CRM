import random


def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))


def is_safe(grid, row, col, num):
    # Check if num is not in the current row
    if num in grid[row]:
        return False

    # Check if num is not in the current column
    if num in (grid[i][col] for i in range(9)):
        return False

    # Check if num is not in the current 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True


def fill_grid(grid):
    numbers = list(range(1, 10))
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                random.shuffle(numbers)
                for num in numbers:
                    if is_safe(grid, i, j, num):
                        grid[i][j] = num
                        if fill_grid(grid):
                            return True
                        grid[i][j] = 0
                return False
    return True


def remove_numbers(grid, num_to_remove):
    attempts = num_to_remove
    while attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while grid[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        backup = grid[row][col]
        grid[row][col] = 0

        copy_grid = [row[:] for row in grid]
        if not solve_sudoku(copy_grid):
            grid[row][col] = backup
            continue

        attempts -= 1


def generate_sudoku():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    fill_grid(grid)
    remove_numbers(grid, 40)  # Remove 40 numbers to make the puzzle
    return grid

# Generate and print the Sudoku puzzle
sudoku_grid = generate_sudoku()
print_grid(sudoku_grid)
