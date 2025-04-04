from flask import Flask, redirect, render_template, request, session
from toolz import diff

from sudoku.table_gen.generate_sudoku import generate_sudoku
from sudoku.table_gen.table_gen import gen_empty_table
from sudoku.verifier.verifier import is_full, is_valid

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.secret_key = "my_v3ry_public_k3y!"


def checkSessionInitialized():
    if "grid" not in session or "moves" not in session or "errorMoves" not in session:
        return redirect("/")


@app.route("/")
def index():
    recordKey = f"allTimeRecord_{session["difficulty"]}"
    # this will work only for local use
    session["grid"] = gen_empty_table()
    session["moves"] = 0
    session["errorMoves"] = 0
    if "difficulty" not in session:
        session["difficulty"] = "easy"
    if recordKey not in session:
        session[recordKey] = 0
    return redirect("/sudoku")


@app.route("/difficulty/<difficulty>")
def difficulty(difficulty):
    session["difficulty"] = difficulty
    return redirect("/")


@app.route("/sudoku/<state>")
@app.route("/sudoku/", defaults={"state": "play"})
def sudoku(state):
    checkSessionInitialized()
    # global grid, moves
    recordKey = f"allTimeRecord_{session["difficulty"]}"

    if state != "win":
        session["grid"] = generate_sudoku(session["difficulty"])
        session["moves"] = 0
        session["errorMoves"] = 0

    if state == "win" and not is_full(session["grid"]):
        return redirect("/sudoku")

    if state == "win" and (session[recordKey] > session["gameTime"] or session[recordKey] == 0):
        session[recordKey] = session["gameTime"]

    return render_template(
        "sudoku-page.html",
        grid=session["grid"],
        state=state,
        winMoves=session["moves"],
        winErrorMoves=session["errorMoves"],
        winGametime=session["gameTime"],
        allTimeRecord=session[recordKey],
        difficulty=session["difficulty"],
    )


@app.route("/get-table")
def get_table():
    # global grid, moves
    session["moves"] = 0
    session["errorMoves"] = 0
    session["grid"] = generate_sudoku(session["difficulty"])
    return render_template("sudoku-table.html", grid=session["grid"])


@app.route("/cell-change/<rowStr>/<colStr>", methods=["POST"])
def check_cell(rowStr, colStr):
    # global grid, moves, errorMoves
    session["moves"] = session["moves"] + 1
    cellStr = request.form.get("cell") if request.form.get("cell") else "0"
    gameTime = request.form.get("gameTime")
    if gameTime != None:
        session["gameTime"] = float(gameTime)

    cell = int(cellStr) if cellStr is not None else 0
    row = int(rowStr) if rowStr is not None else 0
    col = int(colStr) if colStr is not None else 0
    is_valid_cell = is_valid(session["grid"], row, col, cell)

    if not is_valid_cell:
        session["errorMoves"] = session["errorMoves"] + 1
    if is_valid_cell:
        session["grid"][row][col] = cell
        if is_full(session["grid"]):
            return render_template(
                "cell.html",
                row=row,
                col=col,
                cell=cell,
                errorInput=(not is_valid_cell),
                state="winner",
                moves=session["moves"],
                errorMoves=session["errorMoves"],
            )

    return render_template(
        "cell.html",
        row=row,
        col=col,
        cell=cell,
        errorInput=(not is_valid_cell),
        moves=session["moves"],
        errorMoves=session["errorMoves"],
    )


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=5555)
