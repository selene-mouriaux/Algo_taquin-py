import curses
from models import randomize_puzzle, get_correct_puzzle
from console_ui import display_output, clear_ui, handle_keypress


def main():
    """Fonction principale de l'application"""
    try:
        # Récupération d'un taquin tiré aléatoirement
        puzzle = randomize_puzzle(get_correct_puzzle())

        while True:
            # Attend une action et affiche le résultat
            puzzle = handle_keypress(puzzle)
            display_output(puzzle)

            # Frequence de rafraichissement
            curses.napms(50)  # ms
    except KeyboardInterrupt:
        pass
    finally:
        # Lorsqu'on quite, on restaure l'environnement du terminal
        clear_ui()


if __name__ == "__main__":
    main()
