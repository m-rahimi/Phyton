# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 14:38:31 2017

@author: Amin

Input:
   List1: 10->15->4->20
   lsit2:  8->4->2->10
Output:
   Intersection List: 4->10
   Union List: 2->8->20->4->15->10
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked(object):
    def __init__(self, head=None):
        self.head = head
#    @staticmethod
    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next :
                current = current.next
            current.next = node
        return
#    def __new__(self):
#        return self
    
def intersection(linked1, linked2):
    current1 = linked1.head
    current2 = linked2.head
    set1 = set()
    set2 = set()
    
    while current1.next:
        set1.add(current1.value)
        current1 = current1.next
    set1.add(current1.value)
    print set1
    while current2.next:
        set2.add(current2.value)
        current2 = current2.next
    set2.add(current2.value)
    print set2

    set_inter = set1.intersection(set2)
    

    
    linked_inter = Linked()
    for ii in set_inter:
        ee = Node(ii)
        linked_inter.append(ee)
        
    return linked_inter


        
    

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e33 = Node(3)
e4 = Node(4)
e5 = Node(5)
e6 = Node(6)

l1 = Linked(e1)
l1.append(e2)
l1.append(e3)

l2 = Linked(e33)
l2.append(e4)
l2.append(e5)
l2.append(e6)

inter = intersection(l1, l2)


hh = l1.head
for ii in range(7):
    print hh.value
    hh = hh.next


   
