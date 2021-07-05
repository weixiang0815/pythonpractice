# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 20:17:19 2021

@author: henry
"""

import numpy as np

# In[]
ary1 = np.array([1,2,3])
ary2 = np.array([[1,2,3],[4,5,6]])
print(ary1)
print(ary2)
ary3 = np.array([15,"Apple",True])
print(ary3)

# In[]
zero1 = np.zeros((3,))
zero2 = np.zeros((2,3))
print(zero1)
print(zero2)

identity1 = np.eye(1)
identity2 = np.eye(2)
print(identity1)
print(identity2)

one1 = np.ones((3,))
one2 = np.ones((2,3))
const1 = np.full((3,),7)
const2 = np.full((2,3),7)
print(one1)
print(one2)
print(const1)
print(const2)

# In[]
ary1 = np.array([[1,2,3],[4,5,6]])
print(ary1[0,0],ary1[1,2])
ary1[0,0] = 100
ary1[1,2] = 600
print(ary1)

# In[]
ary1 = np.array([[1,2,3],[4,5,6]])
print(type(ary1))
print(ary1.ndim)
print(ary1.shape)
print(ary1.dtype)

# In[]
sample1 = np.arange(0.,5,0.2)
print(sample1)
np.random.shuffle(sample1)
print(sample1)
sample1 = sample1.reshape(5,5)
print(sample1)
sample1 = sample1.astype("unicode")
print(sample1)

# In[]
sample1 = np.linspace(0.,5.,5)
print(sample1)
sample1 = np.logspace(0.,5.,5)
print(sample1)

# In[]
sample2 = np.random.randint(1,7,size=15)
print(sample2)
sample3 = np.random.rand(2,3)
print(sample3)

# In[]
weather = ["Sunny", "Cloudy", "Raining", "Windy"]
Taipei = np.random.choice(weather, size=(4,7), replace=True, p=[0.2, 0.5, 0.2, 0.1])
print(Taipei)
Hsinchu = np.random.choice(weather, size=(4,7), replace=True, p=[0.3, 0.1, 0.1, 0.5])
print(Hsinchu)
Kaohsiung = np.random.choice(weather, size=(4,7), replace=True, p=[0.6, 0.1, 0.1, 0.2])
print(Kaohsiung)

# In[]
normal1 = np.random.randn(3,5)
print(normal1)
normal2 = np.random.normal(10,2,size=(3,5))
print(normal2)

# In[]
dice1 = np.random.randint(1,7, size=15)
print(dice1)
unique1 = np.unique(dice1)
print(unique1)
unique1, count1 = np.unique(dice1, return_counts=True)
print(unique1, count1)
print(dict(zip(unique1, count1)))