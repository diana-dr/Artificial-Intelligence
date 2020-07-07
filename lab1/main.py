#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 22:50:19 2020

@author: dianadragos

main
"""

from words import words
from sudoku import sudoku
from geometric_forms import geometric_forms

def main():
    
    no = 10
    
    while (no != 0):
        print("0. EXIT")
        print("1. Sudoku game")
        print("2. Cryptarithmetic game")
        print("3. Geometric forms")
        
        no = int(input("Choose problem number: "))
        if (no == 1):
            sudoku()
        elif (no == 2):
            words()
        elif (no == 3):
            geometric_forms()
        else:
            return


main()