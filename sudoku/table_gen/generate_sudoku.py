import random
from typing import Literal

from .table_gen import gen_base_table, gen_table

difficulty_to_cells = {
    "supernoob": [9, 9, 8],
    "noob": [5, 4, 4],
    "easy": [4, 3, 3],
    "medium": [3, 3, 3],
    "hard": [3, 2, 2],
    "expert": [2, 2, 2],
}


# utility method to generate a random table
def generate_sudoku(
    difficulty: Literal[
        "supernoob", "noob", "easy", "medium", "hard", "expert"
    ] = "supernoob"
):
    table = gen_table(gen_base_table(), 66)
    visible_cells = difficulty_to_cells[difficulty]

    for outerRow in range(3):
        shuffled = random.sample(visible_cells, len(visible_cells))
        for innerRow, n in enumerate(shuffled):
            n_to_erase = 9 - n
            rowIndex = (outerRow * 3) + innerRow
            while n_to_erase > 0:
                i = random.randint(0, 8)
                if table[rowIndex][i] == 0:
                    continue

                table[rowIndex][i] = 0
                n_to_erase = n_to_erase - 1
    return table
