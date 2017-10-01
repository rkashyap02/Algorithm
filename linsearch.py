def linsearch(x,n):
    """
    ==============
    Linear Search
    ==============
    NAME:
    linearsearch
    
    SYNOPSIS:
    pos = linearsearch(x,element)
    
    DESCRIPTION:
    Program to find the position of a given element in a sorted list
    
    INPUTS:
    x               : Input array
    element         : Element to search
    
    OUTPUTS:
    pos             : Array index of the element to search
    
    AUTHOR:
    Rohit Kashyap, 2015
    """
    for i in range(0,len(x)):
        if x[i] == n:
            return i
