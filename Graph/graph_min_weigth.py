# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 10:27:39 2017

@author: Amin
"""
from collections import defaultdict

def minDistance(graph, node):
    
    length = len(graph)
    conn = defaultdict(list)
    for ii in range(length):
        for jj in range(length):
            if graph[ii][jj] != 0 :
                conn[ii].append([jj, graph[ii][jj]])
                
    
    visited = [node]
    heads = []
    while len(visited) < length:
        
        for ll in conn[node]:
            heads.append(ll[:])
        
        heads = sorted(heads, key=lambda x: x[1], reverse=True)
        
        while True:
            node_dis = heads.pop()
            node = node_dis[0]
            if node not in visited:
                print node
                visited.append(node)
                break
        
        
        
        

graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]];
         
minDistance(graph, 0)