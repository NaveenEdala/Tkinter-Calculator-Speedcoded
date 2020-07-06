# Tkinter-Calculator-Speedcoded
A calculator app I built while learning Tkinter for Python. Speedcoded the entire program in 33 minutes and 57 seconds!

### The following steps were what I took to tackle this project:

1. Planning the layout of the calculator:
    +----------------------+
    |      Input Label     |
    +----------------------+
    |      Output Label    |
    +---+---+----+---+-----+
    | 7 | 8 | 9  | / | DEL |
    +---+---+----+---+-----+
    | 4 | 5 | 6  | * | CLR |
    +---+---+----+---+-----+
    | 1 | 2 | 3  | + |     |
    +---+---+----+---+-----+
    | 0 | . | 00 | - |  =  |
    +---+---+----+---+-----+

2. Assorting positions into rows and columns accourding to Tkinter grid properties

3. Planning functions for Display update, Individual Label update, and Dynamic Calculation

4. Program development
    * Set up Tkinter root panel and main loop
    * Typed functions planned earlier and optimized for rapid calls
    * Initialized labels with columnspans
    * Created buttons and mapped to grid
    * Interlinked functions to respective buttons
    * Optimized memory consumption and label refresh rates by eliminating redundant methods
