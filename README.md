# Conway's Game of Life

![Python implementation](life.gif)

Python implementation of Conway's Game of Life using PyOpenGL. The code includes aswell an implementation of the genetic algorithm described in [Research of Complexity in Cellular Automata
through Evolutionary Algorithms](https://content.wolfram.com/uploads/sites/13/2018/02/17-3-2.pdf), used for finding new rules capable of generating [_spaceship patterns_](https://conwaylife.com/wiki/Spaceship). Read the paper for further information.

This project was part of my  Bachelor's Thesis. To review the project's results you can check chapter 5 of the [thesis report](https://oa.upm.es/71278/1/TFG_GUILLERMO_LOPEZ_GARCIA.pdf).

# Dependencies

Before launching the game or the algorithm you should have previously downloaded `PyOpenGL`. The code works/has been programmed in Python 3.8.

## PyOpenGL

If you are on **Windows**, download [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl) the adecuate PyOpenGL version according to your PC specs and Python version. Then run the next command to complete installation:

```
pip install packagename.whl
```

For example:

```
pip install PyOpenGL‑3.1.6‑cp38‑cp38‑win_amd64.whl

```

For **Linux** users, you can follow [this](https://pypi.org/project/PyOpenGL/) guide.


# How to use it

This repository includes two programs that can be launched: `game.py` and `start.py`.

## game.py
The first one creates a window to visualize a two state (dead or alive) cellular automaton that follows a particular rule. It can be executed with the following commmand:

```
python game.py [rule_name] [window_dimensions] [universe_dimensions]
```

where:
- [rule_name] is the rule's name you want to use for the cellular automaton. That name has to exist on the database.
- [window_dimensions] is the dimensions in pixels that the window will have. For the time being, the X and the Y axis will have the same value, therefore creating a square window.
- [universe_dimensions] is the amount of cells that the univere will contain on each side of the grid.

For instance, if you want to run the Game of Life on a $800\times800$ window and a $100\times100$ grid you should run:

```
python game.py life_rule 800 100
```

This program includes the following key and mouse events to control the graphical interface:

- Left click: when clicking a cell you reverse its state from dead to alive and vice versa.
- "C" key: all the cells change its state to dead.
- "R" key: all the cells change its state to a random one.
- "S" key: similar to the latter one, but this time only with the cells inside a central square of $40 \times 40$ cells.
- "Space" key: stops or resume the program execution.
- "M"  key: inverts the cellular automaton color. By default the alive cells will be white and the dead ones black.
- ⬆ key: increases the execution speed.
- ⬇ key: decreases the execution speed.
- ➡ key: if the execution is stopped, the cellular automaton will evolve to its following state.

Several rules are available and can be tested with the `game.py` command:

- life_rule
- result1
- result2
- result3
- result4
- result5

## start.py

This program is used for running the algorithm mentioned above. It is a genetic algorithm that finds new rules that are capable of generating dinamic patters that can simulate movements across the grid. Again, for further information on how it works check the original [paper](https://content.wolfram.com/uploads/sites/13/2018/02/17-3-2.pdf).

It can be launched by running:

```
python start.py [initial_rule] [result_name] [iterations]
```

where:
- [initial_rule] is the rule that will take the algorithm to create the initial population. It must be a Bay's Space rule, that is, any rule that can be expressed with the format $E_bE_h/F_bF_h$. The paper contains a detailed definition on this term aswell.
- [result_name] is the name which will be used to store the result on the database and that you could later use with the program `game.py`. It should be unique and can not be repeated.
- [iterations] is the maximum number of iterations that the algorithm will execute. Normally it will stop whenever it finds a rule with a propper fitness value, but it has this parameter to avoid endless executions.
