"""Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."


Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
"""

def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low , high):
 
        # If current element is smaller than pivot
        if   arr[j] < pivot:
         
            # increment index of smaller element
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return pivot, i+1 
    
def hindex(arr):
    
    lo = 0
    hi = len(arr) - 1
    print(arr)
    
    print(lo, hi)
    pivot, index = partition(arr, lo, hi)
    print(arr)
    print("PP", pivot, index)
    
    if pivot >= len(arr) - index:
        hi = index - 1
        h = index + 1
    else:
        lo = index + 1
        h = 0
    
    
    if pivot >= len(arr) - index and index == 0:
        print("ll", len(arr))
        return len(arr)
    else:
        print(lo, hi)
        return hindex(arr[lo:hi+1]) + h
        
arr = [8, 9, 5, 2, 1, 3, 9]
hindex(arr)

