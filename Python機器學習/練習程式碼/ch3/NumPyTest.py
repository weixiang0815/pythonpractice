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

# In[]
slice1 = np.random.randint(20, size=20)
print(slice1)
print(slice1[:5])

slice2 = np.random.randint(20, size=(5, 5))
print(slice2)
print(slice2[:3, :3])

# In[]
stat1 = np.arange(1, 11)
print(stat1)

print(stat1.min())
print(stat1.max())
print(stat1.sum())
print(stat1.mean())
print(stat1.std())

# In[]
X1 = np.array([1, 2, 3])
X2 = np.array([20, 36, 40])

print(np.negative(X1))
print(np.add(X1, X2))
print(np.subtract(X1, X2))

# In[]
X1 = np.array([1, 2, 3])
X2 = np.array([20, 36, 40])

print(np.multiply(X1, X2))
print(np.dot(X1, X2))
print(np.inner(X1, X2))
print(np.cross(X1, X2))
print(np.outer(X1, X2))

# In[]
X1 = np.array([1, 2, 3])
X2 = np.array([20, 36, 40])

print(np.divide(X1, X2))
print(np.remainder(X1, X2))

X = np.array([[1, 2], [3, 4]])
Y = np.linalg.inv(X)
print(np.dot(X, Y))

# In[]
X1 = np.array([1, 2, 3])
X2 = np.array([20, 36, 40])
features = np.concatenate((X1, X2)).reshape(2, 3).T
print(features)

# In[]
num1= np.array([-1.67, -1.01, -0.35, 0.97, 1.63])
print(num1)

print(np.around(num1, decimals=1))
print(np.floor(num1))
print(np.ceil(num1))

# In[]
x1 = np.arange(1.0, 10.0, 1.0).reshape(3, 3)
print(x1)

print(np.power(x1, x1))
print(np.exp2(x1))
print(np.exp(x1))
print(np.sqrt(x1))

# In[]
x1 = np.arange(2, 20, 2).reshape(3, 3)
print(x1)

print(np.log10(x1))
print(np.log2(x1))
print(np.log(x1))

# In[]
deg = np.array([0, 30, 60, 90])
rad = np.deg2rad(deg)
print(np.rad2deg(rad))

print(np.sin(deg))
print(np.cos(deg))
print(np.tan(deg))

# In[]
