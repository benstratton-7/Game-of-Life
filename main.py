import numpy as np
import os
from time import sleep
import keyboard
import argparse

step_speed = .17

on = 1
off = 0
states = [on, off]

size_ = None
shape = (size_, size_)
grid = None

#prababilities used for generating a random grid
prob1 = 0.3
prob2 = 0.7
probs = [prob1, prob2]

# Visual boundaries
upperdel = "*"
leftdel = "*"
rightdel = "*\n"
bottomdel = "*"

# On and Off visuals
on_graphic = "#"
off_graphic = " "

# Does the actual new generation step
def update_grid(grid_):
    x_length, y_length = grid_.shape
    updated_grid = np.copy(grid_)
    for coords, current_val in  np.ndenumerate(grid_):
        x_coord, y_coord = coords
        # Gets the coordinates and value of the cell in the specified cardinal direction
        # North
        N_xcoord, N_ycoord = ((x_coord - 1)%x_length, y_coord)
        N_val = grid_[N_xcoord][N_ycoord]
        # North-West
        NW_xcoord, NW_ycoord = ((x_coord - 1)%x_length, (y_coord - 1)%y_length)
        NW_val = grid_[NW_xcoord][NW_ycoord]
        # North-East
        NE_xcoord, NE_ycoord = ((x_coord - 1)%x_length, (y_coord + 1)%y_length)
        NE_val = grid_[NE_xcoord][NE_ycoord]
        # East
        E_xcoord, E_ycoord = (x_coord, (y_coord + 1)%y_length)
        E_val = grid_[E_xcoord][E_ycoord]
        # West
        W_xcoord, W_ycoord = (x_coord, (y_coord - 1)%y_length)
        W_val = grid_[W_xcoord][W_ycoord]
        # South
        S_xcoord, S_ycoord = ((x_coord + 1)%x_length, y_coord)
        S_val = grid_[S_xcoord][S_ycoord]
        # South-West
        SW_xcoord, SW_ycoord = ((x_coord + 1)%x_length, (y_coord - 1)%y_length)
        SW_val = grid_[SW_xcoord][SW_ycoord]
        # South-East
        SE_xcoord, SE_ycoord = ((x_coord + 1)%x_length, (y_coord + 1)%y_length)
        SE_val = grid_[SE_xcoord][SE_ycoord]
        total = NW_val + N_val + NE_val + W_val + E_val + SW_val + S_val + SE_val
        if current_val == 1:
            if total < 2 or total > 3:
                updated_grid[x_coord][y_coord] = 0
            else:
                updated_grid[x_coord][y_coord] = 1
        else:
            if total == 3:
                updated_grid[x_coord][y_coord] = 1
            else:
                updated_grid[x_coord][y_coord] = 0
    np.copyto(grid_, updated_grid)
    return grid_
# Print the grid in a user friendly format
def print_grid(grid_):
    print('Ben\'s Game of Life: "Q" = Quit, "R" = Restart this setup, "N" = New random grid')
    for x in range(size_ + 2):
        print(upperdel, end="")
    print("")
    for i in grid_:
        print(leftdel, end="")
        for j in i:
            if j == 0:
                print(off_graphic, end="")
            if j == 1:
                print(on_graphic, end="")
        print(rightdel, end="")
    for x in range(size_ + 2):
        print(bottomdel, end="")
    print("")

# Starts the game in a terminal
def visual_animation_terminal(initial_grid):
    grid_ = np.copy(initial_grid) # for restart purposes
    switch = True
    os.system("cls")
    while switch:
        print_grid(grid_)
        grid_ = update_grid(grid_)
        sleep(step_speed)
        os.system("cls")
        #extra stuffs
        if keyboard.is_pressed("q"):
            switch = False
        elif keyboard.is_pressed("r"):
            switch = False
            for x in range(2):
                print("Restarting.")
                sleep(.15)
                os.system("cls")
                print("Restarting..")
                sleep(.15)
                os.system("cls")
                print("Restarting...")
                sleep(.15)
                os.system("cls")
            grid_ = initial_grid
            visual_animation_terminal(grid_)
        elif keyboard.is_pressed("n"):
            switch = False
            for x in range(2):
                print("Generating New Grid.")
                sleep(.15)
                os.system("cls")
                print("Generating New Grid..")
                sleep(.15)
                os.system("cls")
                print("Generating New Grid...")
                sleep(.15)
                os.system("cls")
            grid_ = replace_random_grid(grid_.shape)
            visual_animation_terminal(grid_) 
        else:
            pass

def initiate_grid(shape_):
    return np.zeros(shape_, dtype=int)

def add_glider():
    global grid
    grid[7][7] = 1
    grid[8][7] = 1
    grid[8][6] = 1
    grid[8][5] = 1
    grid[6][6] = 1

def spinner():
    global grid
    global size_
    mid = size_//2
    grid[mid][mid] = 1
    grid[mid][mid - 1] = 1
    grid[mid][mid + 1] = 1

def lines():
    global grid
    global size_
    mid = size_//2
    grid[mid][mid] = 1
    grid[mid][mid + 1] = 1
    grid[mid][mid - 1] = 1
    grid[mid][mid + 2] = 1
    grid[mid][mid - 2] = 1
    grid[mid][mid + 3] = 1
    grid[mid][mid - 3] = 1
    grid[mid][mid + 4] = 1
    grid[mid][mid - 4] = 1
    grid[mid][mid + 5] = 1
    grid[mid][mid - 5] = 1
    grid[mid - 2][mid] = 1
    grid[mid - 2][mid + 1] = 1
    grid[mid - 2][mid - 1] = 1
    grid[mid - 2][mid + 2] = 1
    grid[mid - 2][mid - 2] = 1
    grid[mid - 2][mid + 3] = 1
    grid[mid - 2][mid - 3] = 1
    grid[mid - 2][mid + 4] = 1
    grid[mid - 2][mid - 4] = 1
    grid[mid - 4][mid] = 1
    grid[mid - 4][mid + 1] = 1
    grid[mid - 4][mid - 1] = 1
    grid[mid - 4][mid + 2] = 1
    grid[mid - 4][mid - 2] = 1
    grid[mid - 4][mid + 3] = 1
    grid[mid - 4][mid - 3] = 1

def replace_random_grid(shape_):
    return np.random.choice(states, size = shape_,p=probs)

def main():
    global grid
    global size_
    global step_speed
    global on_graphic
    # Allow to adjust starting conditions
    parser = argparse.ArgumentParser(description='Adjust the settings by typing "python main.py " followed by any combination of the below options.\nReplace the [CAPITALIZED] value with your desired value\n')
    parser.add_argument('--size', type=int, default=10, help='Changes the size\n')
    parser.add_argument('--speed', type=float, default=.17, help='Changes the speed\n')
    parser.add_argument('--a', type=str, default='#', help='Changes the cell visual\n')
    parser.add_argument('--i', type=str, default='add_glider', help='Sets the initial conditions\nOptions:\nadd_glider\n')
    args = parser.parse_args()
    func = globals().get(args.i)
    size_ = args.size
    step_speed = args.speed
    on_graphic = args.a
    # Sets the initial grid to be empty
    grid = initiate_grid((size_, size_))
    # Inputs the desired start conditions
    if func:
        func()
    else:
        print(f'Function "{args.i}" not found.')
    # Start animation
    visual_animation_terminal(grid)

if __name__ == '__main__':
    main()