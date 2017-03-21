# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 12:22:20 2017

@author: Amin
"""
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
    
def Search(arr, first, last, target):
    
    mid = (last-first)//2 + first
    if target == arr[mid]:
            return mid
    print first, mid, last
    print arr[first], arr[mid], arr[last]
    if last >= first:
        if arr[first] < arr[mid]: # left is ordered
            print "left"
            if arr[first] <= target and target < arr[mid]:
                return binarySearch(arr[0:mid], 0, mid-1, target)
            else:
                return Search(arr, mid+1, last, target)
        elif arr[mid] < arr[last]:
            print "rigth"
            if arr[mid] < target and target <= arr[last]:
                return binarySearch(arr[mid+1:last+1], 0, last-mid-1, target) + mid + 1
            else:
                return Search(arr, first, mid-1, target)
        else:
            return Search(arr, mid+1, last, target)
    else:
        return -1

            
    

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
x = 2

arr = [8, 9, 10, 1, 2, 3, 5, 6, 7]

arr = [ 2, 3, 4, 10, 40 ]
x = 10
# Function call
result = Search(arr, 0, len(arr)-1, x)
 
if result != -1:
    print "Element is present at index %d" % result
else:
    print "Element is not present in array"
    
binarySearch(arr[0:4], 0, 5, 7)
binarySearch(arr[6:9], 0, 5, 7)


""" C++ format """
class Solution {
public:
  bool search(int A[], int n, int target) {
    int lo =0, hi = n-1;
    int mid = 0;
    while(lo<hi){
          mid=(lo+hi)/2;
          if(A[mid]==target) return true;
          if(A[mid]>A[hi]){
              if(A[mid]>target && A[lo] <= target) hi = mid;
              else lo = mid + 1;
          }else if(A[mid] < A[hi]){
              if(A[mid]<target && A[hi] >= target) lo = mid + 1;
              else hi = mid;
          }else{
              hi--;
          }
          
    }
    return A[lo] == target ? true : false;
  }
};
