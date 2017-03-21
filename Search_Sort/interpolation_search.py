# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 17:48:48 2017

@author: Amin
"""

# Returns index of x in arr if present, else -1
def interpolationSearch (arr, lo, hi, target):
 
    # Check base case
    if hi >= lo:
 
        mid = int(lo + (hi - lo)*(float(target-arr[lo])/(arr[hi]-arr[lo])))
 
        # If element is present at the middle itself
        if arr[mid] == target:
            return mid
         
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > target:
            return interpolationSearch(arr, lo, mid-1, target)
 
        # Else the element can only be present in right subarray
        else:
            return interpolationSearch(arr, mid+1, hi, target)
 
    else:
        # Element is not present in the array
        return -1
    
arr = [ 10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47 ]
x = 42
 
# Function call
result = interpolationSearch(arr, 0, len(arr)-1, x)
 
if result != -1:
    print "Element is present at index %d" % result
else:
    print "Element is not present in array"