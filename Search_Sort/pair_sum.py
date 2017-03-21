# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 18:11:52 2017

@author: Amin
"""

# Python program to check for the sum condition to be satisified
def hasArrayTwoCandidates(A,arr_size,sum):
     
    # sort the array
    quickSort(A,0,arr_size-1)
    l = 0
    r = arr_size-1
     
    # traverse the array for the two elements
    while l<r:
        if (A[l] + A[r] == sum):
            return 1
        elif (A[l] + A[r] < sum):
            l += 1
        else:
            r -= 1
    return 0

def miniDifference(A, arr_size, sum):
    
    # sort the array
    quickSort(A,0,arr_size-1)
    l = 0
    r = arr_size-1
    diff = 111111111 # big number
     
    # traverse the array for the two elements
    while l<r:
        if (abs(A[l] + A[r] - sum) < diff):
            res_l = l
            res_r = r
            diff = abs(A[l] + A[r] - sum)
            print diff
        elif (A[l] + A[r] < sum):
            l += 1
        else:
            r -= 1
    return A[res_l], A[res_r]
    
 
# Implementation of Quick Sort
# A[] --> Array to be sorted
# si  --> Starting index
# ei  --> Ending index
def quickSort(A, si, ei):
    if si < ei:
        pi=partition(A,si,ei)
        quickSort(A,si,pi-1)
        quickSort(A,pi+1,ei)
 
# Utility function for partitioning the array(used in quick sort)
def partition(A, si, ei):
    x = A[ei]
    i = (si-1)
    for j in range(si,ei):
        if A[j] <= x:
            i += 1
             
            # This operation is used to swap two variables is python
            A[i], A[j] = A[j], A[i]
 
        A[i+1], A[ei] = A[ei], A[i+1]
         
    return i+1
     
 
# Driver program to test the functions
A = [1,4,45,6,10,-8]
n = 16
if (hasArrayTwoCandidates(A, len(A), n)):
    print("Array has two elements with the given sum")
else:
    print("Array doesn't have two elements with the given sum")
    
miniDifference(A, len(A), 40)