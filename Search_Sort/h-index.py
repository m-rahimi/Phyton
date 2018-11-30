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
    hindex = 0
    lo = 0
    hi = len(arr) - 1
    
    
    while True:
#        print("LH", lo, hi)
        pivot, index = partition(arr, lo, hi)
#        print(arr)
        hindex = len(arr) - index
#        print("PIH", pivot, index, hindex)
        if pivot > hindex:
#            print("big")
            hi = index - 1
        elif pivot < hindex:
#            print("small")
            lo = index + 1
        else:
#            print("pivot=hindex")
            print(arr)
            return hindex
            
        if lo == hi:
#            print("lo=hi")   
            print(arr)
            hindex = len(arr) - lo
#            print(hindex, lo, arr[lo])
            if arr[lo] >= hindex:
#                print("C1")
                return hindex
            else:
#                print("C2")
                return hindex-1
        # it is a condition if len(arr) <= min(arr)
        if pivot >= len(arr) - index and index == 0:
            return len(arr)
        
arr = [8, 9, 5, 2, 1, 3, 9]
hindex(arr)

arr = [8, 7, 6, 5, 4, 3, 2, 1, 0, 1, 6]
hindex(arr)

