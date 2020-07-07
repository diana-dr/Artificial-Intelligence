#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:19:36 2020

@author: dianadragos

sudoku game

"""

import random

def isSolution(table, n):

    s = 0 
    x = 0
    
    while(n != 0):
        x += n
        n -= 1
    
    for i in range(n):
        for line in table:
            sm += line[i]
        if (sm != x):
            return False
        sm = 0
        
    for line in table:
        for i in line:
            s += i
        if (s != x):
            return False
        s = 0
        
    return True

def sudoku():
    
    # table = [[3, 0, 0, 2], [0, 1, 4, 0], [1, 2, 0, 4], [0, 3, 2, 1]]
    table = [[0, 2, 0, 6, 0, 8, 0, 0, 5], 
            [5, 8, 0, 0, 0, 9, 7, 0, 0], 
            [0, 0, 7, 0, 4, 0, 0, 2, 8], 
            [3, 7, 0, 4, 0, 1, 5, 0, 0], 
            [6, 0, 0, 0, 8, 0, 0, 0, 5], 
            [0, 0, 8, 0, 0, 2, 0, 1, 3], 
            [8, 0, 6, 0, 2, 0, 1, 0, 0], 
            [0, 0, 9, 8, 0, 0, 0, 3, 6], 
            [7, 0, 0, 3, 0, 6, 0, 9, 0]]
    
    num = 9
    a = int(input("How many trials? "))
    
    while (a != 0):
        new_table = []
        for line in table:
            new_line = []
            for i in line:
                if (i != 0):
                    new_line.append(i)
                else:
                    new_line.append(random.randint(1, num))
            new_table.append(new_line)
        a -= 1
        
        if (isSolution(new_table, num)):
            for line in new_table:
                print(str(line))
            break
