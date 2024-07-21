# Several functions for creating vectors

import numpy as np

#function to create nd vectors in (0, 10, 0, 10)\n",
def vec(dim=2):
    return np.random.rand(dim)*10

#function to create row-vectors
def row(dim=2):
    return np.array([vec(dim)])
