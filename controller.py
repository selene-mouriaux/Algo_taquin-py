from models import move, is_correct, get_available_movements, randomize_puzzle, get_correct_puzzle

def make_move(mvt, puzzle):
    possible_moves = get_available_movements(puzzle)
    if mvt in possible_moves:
        move(mvt, puzzle)
    return puzzle

def has_won(puzzle):
    is_correct(puzzle)


def get_puzzle():
    return randomize_puzzle(get_correct_puzzle())

