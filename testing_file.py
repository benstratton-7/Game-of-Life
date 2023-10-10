import numpy as np

# This file is an absolute mess but I wanted to keep it to document how bad my current testing strategy is.
# I know there are much better ways of testing code but I have no clue how to do them at the moment.

#states of cells
on = 1
off = 0
states = [on, off]

#size of grid, "shape_" makes it square, and the grid itself is help by "grid"
size_ = 3
shape_ = (size_,size_)
grid = None

#prababilities used for generating a random grid
prob1 = 0.3
prob2 = 0.7
probs = [prob1, prob2]

#return an empyty grid
def create_empty_grid():
    return np.zeros(shape=shape_, dtype=int)

#return a grid populated
def create_random_grid():
    return np.random.choice(states, size = (size_,size_), p=probs)

#testing function
def print_each_val_in_order(grid):
    for row in grid:
        for col in row:
            print(col)

def trad_python_loops(grid_):
    num_rows, num_cols = grid_.shape
    for row in range(num_rows):
        for col in range(num_cols):
            cur_val = grid_[max(row)][col]
            print(cur_val)

def check_edge(x, y, sizez):
    xlen, ylen = sizez
    return not (x > 0 and x < xlen - 1 and y > 0 and y < ylen - 1)

def check_edge_2(x, y, sizez):
    xlen, ylen = sizez
    if(x <= 0 or x >= xlen - 1 or y <= 0 or y >= ylen - 1):
        return True
    else:
        return False

def surrounding_tiles(grid_):
    size_i = grid_.shape

    for coords, current_pos in  np.ndenumerate(grid_):
        # Splits the coordinate tuple for the current value's location into the x and y coordinates
        x_coord, y_coord = coords
        
        if (check_edge_2(x_coord, y_coord, size_i)):
            print(current_pos, " is an edge")
        else:
            # Gets the coordinates and value of the cell in the specified cardinal direction
            # North
            N_xcoord, N_ycoord = (x_coord - 1, y_coord)
            N_val = grid[N_xcoord][N_ycoord]
            # North-West
            NW_xcoord, NW_ycoord = (x_coord - 1, y_coord - 1)
            NW_val = grid[NW_xcoord][NW_ycoord]
            # North-East
            NE_xcoord, NE_ycoord = (x_coord - 1, y_coord + 1)
            NE_val = grid[NE_xcoord][NE_ycoord]
            # East
            E_xcoord, E_ycoord = (x_coord, y_coord + 1)
            E_val = grid[E_xcoord][E_ycoord]
            # West
            W_xcoord, W_ycoord = (x_coord, y_coord - 1)
            W_val = grid[W_xcoord][W_ycoord]
            # South
            S_xcoord, S_ycoord = (x_coord + 1, y_coord)
            S_val = grid[S_xcoord][S_ycoord]
            # South-West
            SW_xcoord, SW_ycoord = (x_coord + 1, y_coord - 1)
            SW_val = grid[SW_xcoord][SW_ycoord]
            # South-East
            SE_xcoord, SE_ycoord = (x_coord + 1, y_coord + 1)
            SE_val = grid[SE_xcoord][SE_ycoord]
            print("\nX =", current_pos, "")
            print(NW_val, N_val, NE_val, "\n", W_val, " X ", E_val, "\n", SW_val, S_val, SE_val)



grid = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
print("\Test Grid:")
print(grid)
print("\nTests:")

sdot = grid.shape

expected = np.array([1,2,3,4,5,6,10,11,15,16,20,21,22,23,24,25])

for x in range(1, 26):
    # print(grid)
    testx, testy = np.where(grid == x)
    argx = testx[0]
    argy = testy[0]

    print("\nlooking at:          ", x)
    print("coordinates are:     ", argx, argy)
    print("is it an edge?       ", check_edge_2(argx, argy, sdot))
    print("Expected:            ", x in expected)

surrounding_tiles(grid)