# LivingGame

My implementation of Conway's Game of Life. 

## Summary

[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) is a classic cellular automaton simulation. It demonstrates emergent complexity through simple rules governing the states of grid cells—alive or dead.

### Rules
  
  - Any live cell with fewer than two live neighbours dies.
  - Any live cell with more than three live neighbours dies.
  - Any live cell with two or three live neighbours stays alive to the next generation.
  - Any dead cell with exactly three live neighbours will come to life.

# How to Play

You can run this file if you have python installed on your system. Download the file, navigate to the file location, and type "python main.py" and the game should begin with the default settings!
There are many optional parameters that can be passed to this file using GNU syntax. So far you can use the following arguments
    
  * "--speed"  enter a float value that controls how many seconds pass between each generation. Default is .17
  * "--size"  enter an integer value that changes the size of the playing field. Default is 10. Some issues start to arrive with larger sizes based on the size of your terminal but 30 to 40 works well
  * "--a"  enter a single character that will be used as the string for displaying the living cells
  * "--i"  enter a string that will tell the program which function to run to create the starting layout. So far, the following functions are implemented successfully :
    * add_glider
    * spinner
    * lines

### Example

To start a game with a speed of 1 generation every half second, a size of 30X30 grid, use "X" as the living cell representation, and use the "lines" initial starting position, type the following into the terminal
    
    python main.py --speed .5 --size 30 --a X --i lines

## In this Project, I practiced:
  - Data Structures
  - Array Transversal
  - User Input Handling
  - Command Line Arguments

## Reflection
