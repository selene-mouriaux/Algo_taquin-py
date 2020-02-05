from settings import EMPTY_CELL_VALUE, PUZZLE_SIZE

def get_available_movements(puzzle):
    # TODO : retourner une liste de mouvements possibles ["LEFT", "UP"]

    possible_moves = ["UP", "RIGHT", "DOWN", "LEFT"]
    pos_x, pos_y = get_empty_cell_location(puzzle)
    if pos_x == 0:
        possible_moves.remove("UP")
    elif pos_x == PUZZLE_SIZE - 1:
        possible_moves.remove("DOWN")
    if pos_y == 0:
        possible_moves.remove("LEFT")
    elif pos_y == PUZZLE_SIZE -1:
        possible_moves.remove("RIGHT")
    return possible_moves


def move(movement, puzzle):

    possible_moves = get_available_movements(puzzle)
    pos_x, pos_y = get_empty_cell_location(puzzle)
    x2 = pos_x
    y2 = pos_y
    if movement == "UP" and "UP" in possible_moves:
        x2 -= 1
    elif movement == "DOWN" and "DOWN" in possible_moves:
        x2 += 1
    elif movement == "LEFT" and "LEFT" in possible_moves:
        y2 -= 1
    elif movement == "RIGHT" and "RIGHT" in possible_moves:
        y2 += 1
    puzzle[pos_x][pos_y] = puzzle[x2][y2]
    puzzle[x2][y2] = EMPTY_CELL_VALUE

    return puzzle


def get_empty_cell_location(puzzle):
    for x, row in enumerate(puzzle):
        for y, cell in enumerate(row):
            if cell == EMPTY_CELL_VALUE:
                return x, y

