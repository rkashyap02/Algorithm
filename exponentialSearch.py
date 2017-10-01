def binSearch(arr, element, low, high):
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
    element         : Element to search 
    low             : Lower index 
    high            : Higher index bound
    
    OUTPUTS:
    pos             : Index of the element to search
    """    
    while(low <= high):
        # Determine position
        pos = int((low+high)/2)
        # Check if the element lies at center 
        if(arr[pos] == element):
            return  pos
        # Check if the element lies before pos
        elif(arr[pos] > element):
            high = pos -1
        # Check if element lies after pos
        else:
            low = pos +1
        
def exponentialSearch(arr, element):
    """
    ===================
    Exponential Search
    ===================
    NAME:
    exponentialSearch
    
    SYNOPSIS:
    pos = exponentialSearch(arr,element)
    
    DESCRIPTION:
    Program to find the position of a given element in a sorted list
    
    INPUTS:
    x               : Input array
    element         : Element to search for
        
    OUTPUTS:
    pos             : Index of the element to search
    
    AUTHOR:
    Rohit Kashyap, 2015.
    
    """
    
    # Check if the first element is the element we are looking for
    if (arr[0] == element):
        return 0
    # Check if the last element is the element to search
    if (arr[-1] == element):
        return len(arr)-1
    # Initialize 
    i = 1
    # Search for higher bound
    while(arr[i] <= element and i <= len(arr)):
        i = i*2
        # Run binary search after finding the upper bound   
        return binSearch(arr, element, i/2, min(i,len(arr)))
