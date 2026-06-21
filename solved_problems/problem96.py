from pathlib import Path
import numpy as np

def read_problem96_file(path=None):
    path = Path(path) if path is not None else Path(__file__).with_name('problem96.txt')
    with path.open('r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    grids = []
    i = 0
    while i < len(lines):
        if lines[i].startswith('Grid'):
            grid = []
            for j in range(1, 10):
                row = lines[i + j]
                if len(row) != 9 or not row.isdigit():
                    raise ValueError(f'Unexpected sudoku row: {row!r}')
                grid.append([int(ch) for ch in row])
            grids.append(grid)
            i += 10
        else:
            i += 1

    if len(grids) != 50:
        raise ValueError(f'Expected 50 grids, got {len(grids)}')

    return grids

def solve(grid):
    """Solve a Sudoku grid using recursive backtracking.

    The function scans the grid for the first empty cell (represented by 0).
    For that cell it tries every digit from 1 to 9 and checks whether the digit
    is valid in the current grid using the possible() helper. If a digit fits,
    it is placed in the cell and the function calls itself recursively to solve
    the remaining grid. If the recursive call succeeds, the solved grid is kept
    and the function returns True. Otherwise, it resets the cell to 0 and
    continues trying the next digit. When the grid is complete, it prints the
    solved grid and returns True.
    """
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(grid, y, x, n):
                        grid[y][x] = n
                        if solve(grid):
                            return True
                        grid[y][x] = 0
                return False
    print(np.matrix(grid))
    return True

def possible(grid, y, x, n):
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for i in range(0,9) :
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True


def main():
    grids = read_problem96_file()

    print(f'Loaded {len(grids)} sudoku grids')
    total_sum = 0
    for index, grid in enumerate(grids, start=1):
        print(f'Grid {index}')
        for row in grid:
            print(''.join(str(value) for value in row))
        solve(grid)
        number = grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]
        print(f'First three digits of the solved grid: {number}')
        total_sum += number
    print(f'Total sum of the first three digits of all solved grids: {total_sum}')

if __name__ == '__main__':
    main()
