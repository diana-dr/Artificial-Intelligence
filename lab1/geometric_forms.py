#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 08:20:49 2020

@author: dianadragos

3. Geometric forms
"""

import random
import operator

def add_to_table(table, form):
    x = random.randint(0, 4)
    y = random.randint(0, 3)
    
    for coordinate in form:
        if ((x >= 5 and y >= 4) or table[x][y] != 0):
            break
        else:
            table[x][y] = 1
            tuple(map(operator.add, (x, y), coordinate))
            
    return table

def fullyCovered(table):
    
    # for i in range(0, 5):
    #    for j in range(0, 4):
    #        if (table[i][j] == 1):
    #            return False
    return True

def geometric_forms():
    
    table = [[0, 0, 0, 0] for i in range(0, 5)]
    
    patterns = [[(1, 0), (1, 0), (1, 0)],
              [(0, -1), (1, 0), (1, 0)],
              [(1, 0), (1, 0), (0, -1)],
              [(0, -1), (1, 0), (1, 0), (0, 1)],
              [(1, 0), (0, 1), (1, -1)]]
    
    i = int(input("How many trials? "))
    
    for i in range(0, i):
        for form in patterns:
            table = add_to_table(table, form)
    
        if (fullyCovered(table)):
            for line in table:
                print(line)
            print("\n")
    
    print("Cold not find solution!")
    