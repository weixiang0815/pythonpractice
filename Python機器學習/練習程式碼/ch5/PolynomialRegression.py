# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 20:53:30 2021

@author: henry
"""

# In[]
import HappyML.preprocessor as pp

dataset = pp.dataset("C:/Users/henry/Desktop/Python Training/Python機器學習/範例原始碼＆「快樂版」函式庫/Ch05 Regression/Position_Salaries.csv")

X, Y = pp.decomposition(dataset, x_columns=[1], y_columns=[2])

X_train, X_test, Y_train, Y_test = pp.split_train_test(x_ary=X, y_ary=Y, train_size=0.8)

# In[]
from HappyML.regression import SimpleRegressor
import HappyML.model_drawer as md

reg_simple = SimpleRegressor()
Y_simple = reg_simple.fit(x_train=X, y_train=Y).predict(X)

md.sample_model(sample_data=(X, Y), model_data=(X, Y_simple))
print("R-Squared of Simple Regression:", reg_simple.r_score(x_test=X, y_test=Y))

# In[]
from sklearn.preprocessing import PolynomialFeatures

deg = 12
poly_reg = PolynomialFeatures(degree=deg)
X_poly = poly_reg.fit_transform(X)

# In[]
import pandas as pd
regressor = SimpleRegressor()
regressor.fit(X_poly, Y)
Y_predict = regressor.predict(x_test=pd.DataFrame(X_poly))

md.sample_model(sample_data=(X, Y), model_data=(X, Y_predict))

# In[]
from HappyML.performance import rmse

print("Degree: {} RMSE:{:.4f}".format(deg, rmse(Y, Y_predict)))

# In[]
from HappyML.performance import rmse

rmse_linear = rmse(Y, Y_simple)
rmse_poly = rmse(Y, Y_predict)

if rmse_linear < rmse_poly:
    print("RMSE Linear:{:.4f} < RMSE Polynomial:{:.4f}...Linear smaller, WIN!!".format(rmse_linear, rmse_poly))
else:
    print("RMSE Linear:{:.4f} > RMSE Polynomial:{:.4f}...Polynomial smaller, WIN!!".format(rmse_linear, rmse_poly))
