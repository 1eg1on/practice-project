#!/usr/bin/env python3

def hyperbola(x):
    """
    Returns a hyperbola of X given X of type int greater or equal than 1.
    """
    x = int(input())
    if x < 1:
        print('give another x, greater or equal than 1, int')
    else:
        return 1/x
