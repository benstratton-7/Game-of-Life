# living_game

My implementation of Conway's Game of Life. 

## Summary

[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) is a classic cellular automaton simulation. It demonstrates emergent complexity through simple rules governing the states of grid cells—alive or dead.

### Rules
  
  - Any live cell with fewer than two live neighbours dies.
  - Any live cell with more than three live neighbours dies.
  - Any live cell with two or three live neighbours stays alive to the next generation.
  - Any dead cell with exactly three live neighbours will come to life.

# How to Play

## If you have Python installed

You can run the main.py file directly if you have python installed on your system. Download the file, navigate to the file location, and type "python main.py" and the game should begin with the default settings!
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

## If you do not have Python installed

You can still run a basic version of this game using the included executable file. Simply download the files here, navigate to the directory where living_game is installed, then navigate to "executable_materials/living_game/living_game.exe", and run this file. Pyinstaller has packaged all the neccessary dependencies, including a python interpreter, for us, so no need to download anything else!

The only downside of running the app this way is you wont be able to pass any of the optional arguments into the file, so you'll be limitted to the default speed, a 10X10 grid, and using only random layouts.

# Reflection

When I took my second year computer science course almost 4 years ago, we were given the assignment "Implement Conway's Game of Life". Unfortunately for me, I never finished that project and ended up dropping out of Computer Science that semester. When I was thinking of projects I could do to re-teach myself programming, this is one of the first things that popped into my mind. I was always intruiged by the concept, and dissapointed that I never finished the first time around.

I wanted to use this project as a way to get back up to speed with where my programming skills were in the past, but it had the added bonus of re-kindling my passion for building things. I also learned how useful and intuitive python is, and it is now one of my favorite languages to use simply due to it's simplicity. While I still prefer the syntax of other languages like Javascript and C, Pythons usability is top tier in my eyes. I look forward to using python more for more complex projects.

## In this Project, I practiced:
  - Data Structures
  - Array Transversal
  - User Input Handling
  - Command Line Arguments
