# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 18:58:56 2021

@author: henry
"""

# In[]
import numpy as np
import pandas as pd

dataset = pd.read_csv("C:/Users/henry/Desktop/Python Training/Python機器學習/範例原始碼＆「快樂版」函式庫/Ch04 Preprocessing/CarEvaluation.csv")
print(dataset)

# In[]
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 4].values
print(X)
print(Y)

# In[]
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer = imputer.fit(X[:, 1:4])
X[:, 1:4] = imputer.transform(X[:, 1:4])
print(X)

# In[]
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
Y = labelencoder.fit_transform(Y).astype("float64")
print(Y)

# In[]
