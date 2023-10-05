import numpy as np

# print(np.random.choice(states, size = (size_,size_)))
# States of Cells
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