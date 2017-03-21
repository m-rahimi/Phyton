# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 16:05:16 2017

@author: Amin
"""

def findWord(boggle, dic, row, col, visited, word):
    
    
    
    length = 0
    for ss in dic:
        if len(ss) > length:
            length = len(ss)
    
    print length
    visited[row][col] = True
    print visited

    word += boggle[row][col]
    print row, col, word
    if word in dic:
        print word
        return True
    elif len(word) == length:
        visited[row][col] = False
        return
    
    for ii in range(row-1,row+2):
        for jj in range(col-1,col+2):
            if (ii>=0 and jj>=0) and (ii<len(boggle) and jj<len(boggle)) and not visited[ii][jj]:
                if findWord(boggle, dic, ii, jj, visited, word):
                    break
                else:
                    visited[ii][jj] = False
    return False




dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]


boggle = [['G','I','Z'],
          ['U','E','K'],
          ['Q','S','E']]



vi = [[False for ii in range(len(boggle))]for ii in range(len(boggle))]


findWord(boggle, ["GEEKS"], 0, 0, vi, "")

findWord(boggle, ["QUIZ"], 2, 0, vi, "")
