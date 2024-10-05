import numpy as np
import math
"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""

def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    n = 0
    sum = 0
    sumsquared = 0

    #Calculating sum of array
    for i in x:
        n += 1
        sum += i
        sumsquared += i*i
    #computing variance
    var =((1/n)*sumsquared)-((1/n)*sum)**2
    #computing standard deviation
    sd = math.sqrt(var)
    return sd

def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    n = len(x)
    n_sum = sum(x)
    sumsquared = sum(i*i for i in x)
    #compute variance
    var =((1/n)*sumsquared)-((1/n)*n_sum)**2
    #computing standard deviation
    sd = math.sqrt(var)
    return sd

num_lst = [1, 2, 3, 4, 5]
print(std_loops(num_lst))
print(std_builtin(num_lst))
print(np.std(num_lst))
    