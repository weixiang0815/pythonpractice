# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 14:01:49 2021

@author: henry
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import statsmodels.tools.tools as smtools
import statsmodels.api as sm

dataset = pd.read_csv("Insurance.csv")

X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, -1].values

labelencoder = [LabelEncoder(), LabelEncoder()]
X[:, 1] = labelencoder[0].fit_transform(X[:, 1]).astype("float64")
X[:, -2] = labelencoder[1].fit_transform(X[:, -2]).astype("float64")

ary_dummies = pd.get_dummies(X[:, -1]).values
X = np.concatenate((X[:, :-1], ary_dummies), axis=1).astype("float64")

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.01)

sc_X = StandardScaler().fit(X_train)
X_train = sc_X.transform(X_train)
X_test = sc_X.transform(X_test)

X_train = smtools.add_constant(X_train)

# features = [0, 1, 2, 3, 4, 5, 6, 7, 8]
features = [0, 1, 3, 4, 5]
X_opt = X_train[:, features]
regressor_OLS = sm.OLS(exog=X_opt, endog=Y_train).fit()

X_test = smtools.add_constant(X_test)
X_opttest = X_test[:, features]
Y_pred = regressor_OLS.predict(X_opttest)

print("*** FINAL FEATURES:", features)
print("Goodness of Model (Adjusted R2):", regressor_OLS.rsquared_adj)