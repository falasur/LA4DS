# Several handy functions for creating vectors

import numpy as np

def vec(dim=2):
    '''Creates random nd array. Each coordinate is lesser than 10'''
    return np.random.rand(dim)*10

def row(dim=2):
    '''Creates random row-vectors in Rn. Each coordinate lesser than 10'''
    return np.array([vec(dim)])
