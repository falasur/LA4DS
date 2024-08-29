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
    '''Calculates frobenius norm'''
    return np.sum(A**2)**0.5


def frobenius_distance(X, Y):
    return frobenius_norm(X-Y)

def projection(projected, base):
    '''Calculates projection of the projected vector on base'''
    return base*np.dot(projected, base)/np.dot(base,base)

def second_projection (projected, base):
    '''Calculates the projection ortogonal to the base'''
    return projected - projection(projected, base)

def norm(x):
    '''returns vector norm'''
    return sum(x**2)**0.5


def enorm(x, module):
    '''Creates a vector of a given norm in a direction of a given vector'''
    return x * (module / norm(x))


def imatrix(s=2, min=-10, max=10):
    '''Creates random integer square matrix of a given size'''
    return np.random.randint(-10, 10, size=(s,s))

def matrix(s=2):
    '''Creates random normally distributed square matrix of a given size'''
    return np.random.randn(s,s)

def permutation(i,j, size):
    '''Yields a permutation matrix that changes i and j column'''
    P = np.eye(size)
    P[i,i] = 0
    P[j,j] = 0
    P[i,j] = 1
    P[j,i] = 1
    return P