# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
import numpy as np
import scipy.stats as norm
import matplotlib.pyplot as plt


print("Distributions ")
print("1.Bernoulli")
print("2.Uniform")
print("3.Binomial")
print("4.Exponential")

distr = int(input("Choose Distribution: "))
a = int(input("Choose the beginning of the interval: "))
b = int(input("Choose the end of the interval: "))

i = 0
while (i < 3):
    x = random.randint(0, 100)
    y = (-1) * x
    
    domain = np.linspace(x, y, 1000);
    plt.plot(domain, norm.pdf(domain, a, b))
    plt.show()
    i += 1