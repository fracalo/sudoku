import random
from typing import Callable, Dict, List, Tuple

from toolz import compose_left, first

# Define the type for Store
Store = List[List[int]]

# Define the dictionary with typed functions


def gen_base_table():
    return [
        [(c + x * 3 + y) % 9 or 9 for c in range(1, 10)]
        for y in range(0, 3)
        for x in range(0, 3)
    ]


# For generating legit sudoku table we will perform some shuffling,
# we can shuffle:
# - row within the sector (3 element col/rows the col or row belongs to)
# - columns within the sector (3 element col/rows the col or row belongs to)
# - sector row (by sector we mean the 9 outer squares)
# - sector column
#
# we can compose the transpose function with row utils for performing the related column operation
# - column shuffling would become:
#     transpose + row + transpose
# - sector column would become:
#     transpose + sector row + transpose

triplet = [0, 1, 2]


def transpose_store(s: Store) -> Store:
    return [list(row) for row in zip(*s)]


def shuffle_single_row(s: Store) -> Store:
    area = random.choice(triplet)
    loc_org_i, loc_rec_i = random.sample(triplet, 2)

    org_i = loc_org_i + 3 * area
    rec_i = loc_rec_i + 3 * area

    s[org_i], s[rec_i] = s[rec_i], s[org_i]

    return s


def shuffle_square_row(s: Store) -> Store:
    org_i, rec_i = [x * 3 for x in random.sample(triplet, 2)]

    for x in range(3):
        s[org_i + x], s[rec_i + x] = s[rec_i + x], s[org_i + x]

    return s


def swap(s: Store) -> Store:
    a, b = [x for x in random.sample(range(1, 9), 2)]

    for r in s:
        for i, c in enumerate(r):
            if c == a:
                r[i] = b
            if c == b:
                r[i] = a

    return s


# All possible shuffle methods are contained in shuffler
shufflers: Dict[str, Tuple[Callable[[Store], Store], float]] = {
    "swap": (swap, 0.4),
    "row": (shuffle_single_row, 0.15),
    "col": (compose_left(transpose_store, shuffle_single_row, transpose_store), 0.15),
    "square_row": (shuffle_square_row, 0.15),
    "square_col": (
        compose_left(transpose_store, shuffle_square_row, transpose_store),
        0.15,
    ),
}

shufflers_weights = [weight for (_, weight) in shufflers.values()]


# in order to generate a table we randomly choose a shuffler and process the store
def gen_table(org_table: Store, iterations: int) -> Store:
    if iterations == 0:
        return org_table

    shuffler_name = first(
        random.choices([x for x in shufflers.keys()], weights=shufflers_weights, k=1)
    )

    shuffler, _ = shufflers[shuffler_name]
    return gen_table(shuffler(org_table), iterations - 1)


def gen_empty_table():
    table = []
    for x in range(9):
        row = []
        table.append(row)
        for x in range(9):
            row.append(0)
    return table
