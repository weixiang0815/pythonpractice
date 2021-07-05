# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 21:14:26 2021

@author: henry
"""

import numpy as np

dice = [1, 2, 3, 4, 5, 6]
prob = [0.1, 0.1, 0.2, 0.1, 0.2, 0.3]
roll = np.random.choice(dice, size=100, replace=True, p=prob)
print("擲出 100 次不公正骰子的結果:")
print(roll)
print("各點數出現機率:")
theory = dict(zip(dice, prob))
print("理論機率:", theory)
unique, counts = np.unique(roll, return_counts=True)
reality = dict(zip(unique, counts / 100))
print("實際機率:", reality)
