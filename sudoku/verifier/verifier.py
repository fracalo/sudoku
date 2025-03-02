# solution description:
# every number participates in 3 sectors that need to contain 9 different numbers (1 through 9),
# the sectors in total are 27 (9 rows, 9 columns, plus the 9 inner squares),
# each sector can be classified as a dictionary with keys 1 through 9,
# if one of the sectors happens to have a duplicate key the output will be false, otherwise true
#
# how do we identify the sectors?
# identifying rows and columns is trivial (we check the y and x index)
#
# identifying the inner square sector could be done based on a 2level 1 through 3 nested dictionary,
# we'll identify the corresponding x and y square position based on the result of floor(index / 3)
# visualization of the inner square store sectors:
#  -------------------
#  | 0-0 | 0-1 | 0-2 |
#  -------------------
#  | 1-0 | 1-1 | 1-2 |
#  -------------------
#  | 2-0 | 2-1 | 2-2 |
#  -------------------
#
# Note: we're not doing validation on the input numbers, we trust them to be a number > 0 and < 10

from math import floor

from ..table_gen.table_gen import Store


def verifier(o):
    # this is what the inner square store should look like
    squareStore = {y: {x: {} for x in range(0, 3)} for y in range(0, 3)}
    # we also prepare a store for the columns
    colStores = {y: {} for y in range(0, 9)}

    for iy, row in enumerate(o):
        # we also prepare a store for the row
        rowStore = {}
        # we conserve the innerSquare outerIndex, will be used afterwards during the squareStore check
        outerSqIndex = floor(iy / 3)
        for ix, x in enumerate(row):

            # we retrieve the innerSquare innerIndex
            innerSqIndex = floor(ix / 3)

            # we check the column, row and innerSquare store
            if (
                x in rowStore
                or x in colStores[ix]
                or x in squareStore[outerSqIndex][innerSqIndex]
            ):
                return False

            # we add the value to all relevant stores
            colStores[ix][x] = True
            rowStore[x] = True
            squareStore[outerSqIndex][innerSqIndex][x] = True

    return True


def partial_verifier(o):
    # this is what the inner square store should look like
    squareStore = {y: {x: {} for x in range(0, 3)} for y in range(0, 3)}
    # we also prepare a store for the columns
    colStores = {y: {} for y in range(0, 9)}

    for iy, row in enumerate(o):
        # we also prepare a store for the row
        rowStore = {}
        # we conserve the innerSquare outerIndex, will be used afterwards during the squareStore check
        outerSqIndex = floor(iy / 3)
        for ix, x in enumerate(row):

            # if the cell is not set we can continue
            if x is not None:
                continue

            # we retrieve the innerSquare innerIndex
            innerSqIndex = floor(ix / 3)
            # we check the column, row and innerSquare store
            if (
                x in rowStore
                or x in colStores[ix]
                or x in squareStore[outerSqIndex][innerSqIndex]
            ):
                return False

            # we add the value to all relevant stores
            colStores[ix][x] = True
            rowStore[x] = True
            squareStore[outerSqIndex][innerSqIndex][x] = True

    return True


def is_valid(board: Store, row: int, col: int, num: int):
    """Check if placing num at board[row][col] is valid."""
    for i in range(9):
        # Check row and column
        if board[row][i] == num or board[i][col] == num:
            return False
        # Check 3x3 subgrid
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
            return False
    return True


def is_full(board: Store):
    """Check if placing num at board[row][col] is valid."""
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return False
    return True


# def is_unique_solution(board):
#    """
#    Check if a given Sudoku board has a unique solution.
#
#    Args:
#    - board (list[list[Optional[int]]]): A 9x9 Sudoku board represented as a list of lists.
#      None represents an empty cell.
#
#    Returns:
#    - bool: True if the board has exactly one solution, False otherwise.
#    """
#
#    def solve(board, solutions_count):
#        """Solve the Sudoku board, tracking the number of solutions."""
#        for row in range(9):
#            for col in range(9):
#                if board[row][col] is not None:  # Empty cell
#                    for num in range(1, 10):  # Numbers 1-9
#                        if is_valid(board, row, col, num):
#                            board[row][col] = num  # Try placing the number
#                            if solve(board, solutions_count):  # Recursive call
#                                solutions_count[0] += 1
#                                if solutions_count[0] > 1:  # More than one solution
#                                    return False
#                            board[row][col] = None  # Backtrack
#                    return False  # No valid number found, backtrack
#        return True  # Solved
#
#
# solutions = 0
#
#
# def count_solutions(grid):
#    solution_count = 0
#
#    def count(grid):
#        nonlocal solution_count
#        for row in range(9):
#            for col in range(9):
#                if grid[row][col] is not None:
#                    for num in range(1, 10):
#                        if not is_valid(grid, row, col, num):
#                            continue
#
#                        grid[row][col] = num
#                        count(grid)
#                    return
#        solution_count += 1
#
#    count(grid)
#    return solution_count
