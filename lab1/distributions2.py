# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    print("Distributions ")
    print("1.Normal")
    print("2.Geometric")
    
    distr = int(input("Choose Distribution: "))
    # a = int(input("Choose the beginning of the interval: "))
    # b = int(input("Choose the end of the interval: "))
    
    mu = 0
    sigma = 0.1
    
    if (distr == 1):
        x = np.random.normal(mu, sigma, 10000)
        y = (1 / (np.sqrt(2 * np.pi * np.power(sigma, 2)))) * \
        (np.power(np.e, - (np.power((x - mu), 2) / (2 * np.power(sigma, 2)))))
        
        plt.plot(x, y)
        plt.show()
        
    elif (distr == 2):
        x = np.random.geometric(p = 0.35, size = 10000)
        plt.plot(x)
        plt.show()
        
    else:
        return
    
main()