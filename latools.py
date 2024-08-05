# Several handy functions for creating vectors

import numpy as np

def vec(dim=2):
    '''Creates random nd array. Each coordinate is lesser than 10'''
    return np.random.rand(dim)*10

def row(dim=2):
    '''Creates random row-vectors in Rn. Each coordinate lesser than 10'''
    return np.array([vec(dim)])


def column(dim=2):
    '''Creates random column-vectors in Rn. Each coordinate lesser than 10'''
    return row(dim).T

def frobenius_norm(A):
    return np.sum(A**2)**0.5


def frobenius_distance(X, Y):
    return frobenius_norm(X-Y)
