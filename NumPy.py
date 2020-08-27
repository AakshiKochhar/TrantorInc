""" This program will use NumPy to mean normalize an ndarray  and separate it into several smaller ndarrays."""

import numpy
from numpy.random import randint
        
def normalize_array(array, axis):
    """
        This function receives an MxN array (matrix) and normalizes it, according to the specified axis
        If axis = 0, each row of the matrix will be normalized
        If axis = 1, each column will be normalized
        
        This function returns a list of arrays, containing the normalized values.
        The size of the returned list will depend of the axis of normalization
    """

    
    ret = list()
    if axis == 0: 
        for i in range(len(array)): 
            row = arr[i,:] # Extract row i
            row = (row - numpy.min(row))/(numpy.max(row)-numpy.min(row))
            ret.append(row) # Append the normalized row to the list that will be returned by the function
    elif axis == 1: 
        for i in range(len(array[0])): # Iterate through each column
            col = array[i,:] 
            col = (col - numpy.min(col))/(numpy.max(col)-numpy.min(col)) # Normalize
            ret.append(col) 
    
    # Take the list 'ret' and split it into a list of ndarrays
    return numpy.split(numpy.array(ret), len(ret))
