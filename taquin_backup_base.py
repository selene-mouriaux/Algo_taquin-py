import random
from terminaltables import AsciiTable
import curses


GAME_TITLE = "`•.,¸¸ [ JEU DU TAQUIN ] ¸¸,.•´"

# Nombre de cases par côté
TAQUIN_SIZE = 4

# Valeur de la case vide
EMPTY_CASE_VALUE = ""


# Taquin correct, dans l'ordre
CORRECT_SOLUTION = [list(a) for a in zip(*[iter(list(range(1, TAQUIN_SIZE ** 2)) + [EMPTY_CASE_VALUE])] * TAQUIN_SIZE)]


def get_available_movements():
    # TODO : retourner une liste de mouvements possibles ["LEFT", "UP"]
    return []


def move(direction, state):
    # TODO :
    # * récupérer les mouvements possibles pour l'état en cours
    # * appliquer le mouvement si c'est permis
    # * retourner l'état modifié
    return state


def has_won(state):
    # TODO : vérifier si le jeu est gagné
    pass


def get_random_state():
    # TODO : certains états random ne sont pas solvables,
    # il faut que cette fonction ne renvoie que des états solvables
    cases = list(range(1, TAQUIN_SIZE ** 2)) + [EMPTY_CASE_VALUE]
    random.shuffle(cases)
    return [list(a) for a in zip(*[iter(cases)] * TAQUIN_SIZE)]


def echo(data, ui):
    """
    Utilitaire pour afficher une donnée à l'écran.
    Peut être utilisée pour afficher des informations de debug

    * data (str) : la donnée à afficher
    * ui (curse Window) : la UI sur laquelle afficher l'info
    """
    x = 10 + TAQUIN_SIZE * 2
    ui.addstr(x, 0, "%s  " % data)
    ui.refresh()


def handle_keypress(state, ui):
    try:
        key = ui.getkey().upper()
    except Exception:
        return state

    height, width = ui.getmaxyx()

    if key == "KEY_DOWN":
        ui.addstr(height - 1, 0, "↓ DOWN - A FAIRE", curses.A_REVERSE)
        state = move("DOWN", state)

    elif key == "KEY_UP":
        ui.addstr(height - 1, 0, "↑ UP - A FAIRE", curses.A_REVERSE)
        state = move("UP", state)

    elif key == "KEY_LEFT":
        ui.addstr(height - 1, 0, "← LEFT - A FAIRE", curses.A_REVERSE)
        state = move("LEFT", state)

    elif key == "KEY_RIGHT":
        ui.addstr(height - 1, 0, "→ RIGHT - A FAIRE", curses.A_REVERSE)
        state = move("RIGHT", state)

    elif key in ("Q",):
        raise KeyboardInterrupt

    return state


def get_state_as_str(state):
    table = AsciiTable(state)
    table.inner_heading_row_border = False
    table.inner_row_border = True
    table.justify_columns[0] = "center"
    table.justify_columns[1] = "center"
    return table.table


def display_output(state, ui):
    # Title
    ui.addstr(0, 0, GAME_TITLE, curses.color_pair(1))

    # Table game
    ui.addstr(2, 0, get_state_as_str(state), curses.color_pair(1))

    # Controls
    ui.addstr(4 + TAQUIN_SIZE * 2, 0, "Utiliser les flêches pour déplacer la case vide.")
    ui.addstr(5 + TAQUIN_SIZE * 2, 0, "(r)eset | (s)olution | (c)ancel | (q)uitter")

    if has_won(state):
        ui.addstr(
            7 + TAQUIN_SIZE * 2,
            0,
            "🎉 🎺 🎺  V O U S   A V E Z   G A G N É   ! !  🎺 🎺 🎉",
            curses.color_pair(2) | curses.A_BLINK,
        )
    ui.refresh()


def init_ui():
    ui = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.noecho()
    ui.keypad(True)
    ui.nodelay(True)
    return ui


def clear_ui(ui):
    curses.nocbreak()
    ui.keypad(False)
    curses.echo()
    curses.endwin()


def main():
    """Fonction principale de l'application"""
    try:
        # Initalisation de l'UI
        ui = init_ui()

        # Récupération d'un taquin tiré aléatoirement
        state = get_random_state()

        while True:
            # Attend une action et affiche le résultat
            state = handle_keypress(state, ui)
            display_output(state, ui)

            # Frequence de rafraichissement
            curses.napms(50)  # ms
    except KeyboardInterrupt:
        pass
    finally:
        # Lorsqu'on quite, on restaure l'environnement du terminal
        clear_ui(ui)


if __name__ == "__main__":
    main()
