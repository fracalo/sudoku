from flask import Flask, redirect, render_template, request

from sudoku.table_gen.generate_sudoku import generate_sudoku
from sudoku.table_gen.table_gen import gen_empty_table
from sudoku.verifier.verifier import is_full, is_valid

app = Flask(__name__)

# this will work only for local use
grid = gen_empty_table()
moves = 0
errorMoves = 0


@app.route("/")
def index():
    return redirect("/sudoku")


@app.route("/sudoku/", defaults={"state": "play"})
@app.route("/sudoku/<state>")
def sudoku(state):
    global grid, moves
    if state != "win":
        grid = generate_sudoku()
        moves = 0
    if state == "win" and not is_full(grid):
        return redirect("/sudoku")
    return render_template("sudoku-page.html", grid=grid, state=state)


@app.route("/get-table")
def get_table():
    global grid, moves
    moves = 0
    grid = generate_sudoku()
    return render_template("sudoku-table.html", grid=grid)


# @app.route("/check-table")
# def check_table():
#    global grid
#    print(grid)
#    return "ciao"


@app.route("/cell-change/<rowStr>/<colStr>", methods=["POST"])
def check_cell(rowStr, colStr):
    global grid, moves, errorMoves
    moves = moves + 1
    cellStr = request.form.get("cell") if request.form.get("cell") else "0"
    gameTime = request.form.get("gameTime")

    cell = int(cellStr) if cellStr is not None else 0
    row = int(rowStr) if rowStr is not None else 0
    col = int(colStr) if colStr is not None else 0
    is_valid_cell = is_valid(grid, row, col, cell)

    print(f"nononon {is_valid_cell}")
    if not is_valid_cell:
        errorMoves = errorMoves + 1
        print(errorMoves)
    if is_valid_cell:
        grid[row][col] = cell
        if is_full(grid):
            return render_template(
                "cell.html",
                row=row,
                col=col,
                cell=cell,
                errorInput=(not is_valid_cell),
                state="winner",
                moves=moves,
                errorMoves=errorMoves,
            )

    return render_template(
        "cell.html",
        row=row,
        col=col,
        cell=cell,
        errorInput=(not is_valid_cell),
        moves=moves,
        errorMoves=errorMoves,
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5555)
