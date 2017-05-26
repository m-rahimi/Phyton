# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 11:57:52 2017
@author: Amin
"""

def findLongestFromACell(grid, row, col, mem):
    
    nrow = len(grid)
    ncol = len(grid[0])    
    cout = 0
    for ii in range(row-1,row+2):
        for jj in range(col-1,col+2):
            if not (ii == row and jj == col) and (ii >= 0 and ii <nrow) and \
                   (jj >= 0 and jj < ncol) and not (abs(row-ii) == abs(col-jj)):

                if mem[ii][jj] == -1 and grid[ii][jj] - grid[row][col] == 1:
                    cout += findLongestFromACell(grid, ii, jj, mem) + 1
                    mem[ii][jj] = cout
                elif mem[ii][jj] > 0 and grid[ii][jj] - grid[row][col] == 1:
                    cout += mem[ii][jj]

    return cout
                    
                    
                
def finLongestOverAll(grid):
    nrow = len(grid)
    ncol = len(grid[0]) 
    
    mem = [[-1 for ii in range(jj,jj+ncol)] for jj in range(0,ncol*nrow,ncol)]
    
    dis = []
    for ii in range(nrow):
        for jj in range(ncol):
            temp = findLongestFromACell(grid, ii, jj, mem)
            dis.append(temp)
    
    return max(dis) + 1


a = [[1, 2, 9],
     [5, 3, 8],
     [4, 6, 7]]

finLongestOverAll(a)

#findLongestFromACell(a, 2 , 0, mem)
