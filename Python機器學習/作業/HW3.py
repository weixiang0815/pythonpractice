# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 11:40:19 2021

@author: henry
"""

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

dataset = pd.read_csv("HealthCheck.csv")

X = dataset.iloc[:, :-1]
Y = dataset.iloc[:, -1]

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer = imputer.fit(X.iloc[:, 1:3])
X.iloc[:, 1:3] = imputer.transform(X.iloc[:, 1:3])

labelencoder = LabelEncoder()
Y = labelencoder.fit_transform(Y).astype("float64")

ary_dummies = pd.get_dummies(X["Race"]).values
X = np.concatenate((ary_dummies, X.iloc[:, 1:3]),axis = 1).astype("float64")

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

sc_X = StandardScaler().fit(X_train)
X_train = sc_X.transform(X_train)
X_test = sc_X.transform(X_test)

print("自變數訓練集：")
print(X_train)
print("應變數訓練集：", Y_train)
print("自變數測試集：")
print(X_test)
print("應變數測試集：", Y_test)
