def jumpsearch(arr, element, step):
    """
    ============
    Jump Search
    ============
    NAME:
    jumpsearch
    
    SYNOPSIS:
    pos = jumpsearch(arr, element, step)
    
    DESCRIPTION:
    Program to find the position of a given element in a sorted list
    
    INPUTS:
    arr             : Input array
    element         : Element to search
    step            : Steps in which to jump across data
    
    OUTPUTS:
    pos             : Array index of element to search
    
    AUTHOR:
    Rohit Kashyap,2015
    """
    # Check for a valid input array
    if len(arr) == 0:
        return "Check the input array"
    # Check for a valid step size
    if step >= len(arr):
        return "Step size too large"
    # Check initially if element is present or not
    if element > arr[-1]:
        return "Element not found"
    # Jump in steps
    for i in range(1,len(arr)//step+1):    
        if(arr[i*step] > element):
            #Perform Linear search once step is determined
            for j in range((i-1)*step, step*i+1):
                if(arr[j] == element):
                    return j
    #Search for the remaining elements
    left = (len(arr)//step)*step 
    #Perform Linear search
    for i in range(left, len(arr)):
        if(arr[i] == element):
            return i
    return None
                    
    
