def interpolation(arr, element):
    """
    =====================
    Interpolation Search
    =====================
    NAME:
    interpolation
    
    SYNOPSIS:
    pos = interpolation(arr, element)
    
    DESCRIPTION:
    Program to find the position of a given element in a sorted list
    
    INPUTS:
    arr             : Input array
    element         : Element to search
     
    OUTPUTS:
    pos             : Array index of element to search
    
    AUTHOR:
    Rohit Kashyap,2015
    """
    # Check if its a valid input array
    if(len(arr) < 1):
        return "Check the input array"
    low, high = 0, len(arr)-1
    # Run the loop sufficiently
    while(low <= high):
        pos = int(low + ((element-arr[low])*(high-low)/ (arr[high]-arr[low])))
        # See if element is found in position position
        if(arr[pos] == element):
            return pos
        # Element is above position
        elif(x > pos):
            low = pos +1
        # Element is below position
        else:
            high = pos -1
    return None
