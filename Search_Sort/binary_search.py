# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 11:44:19 2017

@author: Amin
"""

def binarySearch(arr, first, last, target):
    
    mid = (last-first)//2 + first
    if target == arr[mid]:
       result = mid
    elif last - first < 2:
        if target == arr[first]:
            result = first
        elif target == arr[last]:
            result = last
        else:
            result = -1
    elif target > arr[mid]:
       result = binarySearch(arr, mid, last, target)
    elif target < arr[mid]:
       result = binarySearch(arr, first, mid, target)
    return result

# Returns index of x in arr if present, else -1
def binarySearch (arr, l, r, x):
 
    # Check base case
    if r >= l:
 
        mid = l + (r - l)/2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
         
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binarySearch(arr, mid+1, r, x)
 
    else:
        # Element is not present in the array
        return -1

# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 30
 
# Function call
result = binarySearch(arr, 0, len(arr)-1, x)
 
if result != -1:
    print "Element is present at index %d" % result
else:
    print "Element is not present in array"