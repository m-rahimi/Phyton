# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 15:47:55 2017

@author: Amin
"""

#A naive recursive implementation of 0-1 Knapsack Problem
 
# Returns the maximum value that can be put in a knapsack of
# capacity W
# 2^n complexity
def knapSack(W , wt , val , n):
 
    # Base Case
    if n == 0 or W == 0 :
        return 0
 
    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    print wt[n-1]
    if (wt[n-1] > W):
        return knapSack(W , wt , val , n-1)
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1),
                   knapSack(W , wt , val , n-1))
 
# end of function knapSack
 
# To test above function
val = [60, 100, 120, 20]
wt = [10, 20, 70, 5]
W = 60
n = len(val)
print knapSack(W , wt , val , n)
 

# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
 
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
 
    return K[n][W]
 
# Driver program to test above function
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack(W, wt, val, n))



def subsetIndex(length, indx, m=0):
    if length == m:
        return

    for ii in range(m, length):
        indx.append(ii)
#        indx2 = indx
#        for jj in indx:
#            indx2.append(jj)
#        print indx2
        if indx :
            indx2.append(indx[:])
        print indx
        if ii < length-1:
            subsetIndex(length, indx, ii+1)
              
        indx.pop()
       
indx = []
indx2 = []
subsetIndex(3, indx, 0)

a = []
b = [2, 3]
a.append(b)
c = [3, 4]
a.append(c)
d = [1, 3, 5]
a.append(d)

def knapSack(W, wt, val, m, n, indx):
    if n == m:
        return 0
    print "***"
    for ii in range(m,n):
        indx.append(ii)
        if ii<n-1:
            knapSack(W, wt, val, ii+1, n, indx)
        print indx, ii
 #       ss = 0; sum_wt = 0
#        for jj in indx:
#            ss += val[jj]
 #           sum_wt += wt[jj]
        indx.pop()
        
        #return max(max_old, ss) if sum_wt <= W else 0
        
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
indx = []
#wt.append(0)
#val.append(0)
print(knapSack(W, wt, val, 0, 5, indx))

indx=[0, 2]
val[indx]
            
        
