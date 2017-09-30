def binsearch(arr, element):
    """
    ==============
    Binary Search
    ==============
    NAME:
    binsearch
    
    SYNOPSIS:
    pos = binsearch(x,element)
    
    DESCRIPTION:
    Program to find the position of a given element in a sorted list
    
    INPUTS:
    x               : Input array
    
    OUTPUTS:
    element         : Element to search
    
    AUTHOR:
    Rohit Kashyap,2015
    """

    low, high = 0, len(arr) -1
    while(low <= high):
        mid = (low + high) // 2
        if(element > arr[mid]):
            low = mid + 1 
        elif(element < arr[mid]):
            high = mid - 1
        else:
            return mid
    return "Element not found"
