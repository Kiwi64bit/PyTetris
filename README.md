# Ketris

A knock-off version of, the famous classic game, Tetris using **python** and **curses** module.

## How to run the game?
This is A terminal game, so we'll be using the terminal.

### on Unix (Linux/macOS)
The curses module is Unix based and already comes with python.
All you need to do is to open the game directory in the terminal and run the following command.

```bash
python main.py
```
or
```bash
python3 main.py
```

### on windows
There is another version of the **curses** module called **windows-curses**, which does not come with python, so we have to install it.
You can install **windows-curses** using python's package manager [pip](https://pip.pypa.io/en/stable/) using the following command.

```bash
pip install windows-curses
```
or
```bash
python3 -m pip install windows-curses
```


You can now open the game directory in the terminal and run the next command.
```bash
python main.py
```
## Gameplay

1. Control the snake using arrow keys (Up to rotate, Left/Right to move, Down to soft drop).
2. The objective is to clear rows and get the highest score. 
3. If there is no place for a new piece to spawn, you lose.

## Key features

* Modular script: using classes that makes adding new features easy.
* Classic terminal game. no GUI is needed.

## What's next?

* A menu screen for starting the game and changing sittings.
* New features: Hold, hard drop, next piece, difficulty progression.
* Better interface
* Speed options to control the game difficulty.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
