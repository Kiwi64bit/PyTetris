import curses
from pytetris import PyTetris


def main(stdscr: curses.window) -> None:
    py_tetris: PyTetris = PyTetris(
            grid_size=(10, 20),
            key_bindings={
                    curses.KEY_LEFT : 'left',
                    curses.KEY_RIGHT: 'right',
                    curses.KEY_UP   : 'rotate',
                    curses.KEY_DOWN : 'soft_drop',
            },
    )
    py_tetris.main(stdscr)


if __name__ == '__main__':
    curses.wrapper(main)
