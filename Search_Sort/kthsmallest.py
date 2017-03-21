# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 18:26:59 2017

@author: Amin
"""

def kthsmallest(arr, k):
    n = len(arr) 
    print arr
    print k
    pivot = arr[n-1]     # use as a pivot
    small = []
    large = []
    
    for ii in arr:
        if ii < pivot:
            small.append(ii)
        elif ii > pivot:
            large.append(ii)
    
    if len(small)+1 == k:
        return pivot
    if len(small) == 1 and k == 1:
        return small[0]
    if len(small) > k:
        return kthsmallest(small, k)
    elif len(small) < k:
        return kthsmallest(large, k-len(small)-1)
    elif len(small) == k:
        return kthsmallest(small, k)
        
        
        
arr2 = [12, 3, 5, 7, 4, 19, 26, 1, 30, 15, 45, 33]
kthsmallest(arr2, 7)

arr.sort()