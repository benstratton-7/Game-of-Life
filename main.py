import numpy as np
import os
from time import sleep
import keyboard

# print(np.random.choice(states, size = (size_,size_)))
# States of Cells
on = 1
off = 0
states = [on, off]

#size of grid, "shape_" makes it square, and the grid itself is held by "grid"
size_ = 10
grid = None

#prababilities used for generating a random grid
prob1 = 0.3
prob2 = 0.7
probs = [prob1, prob2]

def initialize_grid():
    global grid
    grid = np.random.choice(states, size = (size_,size_),p=probs)


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
        if total == 2 or total == 3:
            updated_grid[x_coord][y_coord] = 1
        else:
            updated_grid[x_coord][y_coord] = 0
    np.copyto(grid_, updated_grid)
    return grid_

def start_animation_terminal():
    global grid
    switch = True
    while switch:
        os.system("cls")
        print("Ben's Game of Life: press ctrl+C to quit")
        print(grid)
        grid = update_grid(grid)
        sleep(.5)

def other_terminal_animation():
    global grid
    switch = True
    while switch:
        os.system("cls")
        for i in grid:
            for j in i:
                if j == 0:
                    print(" ", end="")
                if j == 1:
                    print("#", end="")
            print("\n", end="")
        grid = update_grid(grid)
        sleep(.15)

initialize_grid()
grid = np.zeros((15,15))
grid[7][7] = 1
grid[8][7] = 1
grid[9][7] = 1
other_terminal_animation()