# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 19:58:29 2021

@author: henry
"""

# In[]
import HappyML.preprocessor as pp

dataset = pp.dataset(file="C:/Users/henry/Desktop/Python Training/Python機器學習/範例原始碼＆「快樂版」函式庫/Ch04 Preprocessing/CarEvaluation.csv")
print(dataset)

# In[]
X, Y = pp.decomposition(dataset, x_columns=[i for i in range(4)], y_columns=[4])
print(X)
print(Y)

# In[]
X = pp.missing_data(X, strategy="mean")
print(X)

# In[]
Y = pp.label_encoder(Y)
print(Y)

Y, Y_mapping = pp.label_encoder(Y, mapping=True)
print(Y)
print(Y_mapping)

# In[]
