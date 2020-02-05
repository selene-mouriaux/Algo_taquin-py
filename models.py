from random import shuffle, choice
from settings import PUZZLE_SIZE, EMPTY_CELL_VALUE
from controller import get_available_movements, move


def has_won(puzzle):
    # TODO : vérifier si le jeu est gagné
    pass

def randomize_puzzle(puzzle, difficulty=10):
    # TODO : certains états random ne sont pas solvables,
    # il faut que cette fonction ne renvoie que des états solvables

    for n in range(difficulty):
        possible_moves = get_available_movements(puzzle)
        movement = choice(possible_moves)
        puzzle = move(movement, puzzle)

    return puzzle


def get_correct_puzzle():
    # Taquin correct, dans l'ordre
    return [list(a) for a in zip(*[iter(list(range(1, PUZZLE_SIZE ** 2)) +
                                        [EMPTY_CELL_VALUE])] * PUZZLE_SIZE)]


[list(a) for a in zip(*[iter(list(range(1, 16)) + [""])] * 4)]