# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 20:53:59 2021

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
from HappyML.regression import PolynomialRegressor

reg_poly = PolynomialRegressor()
reg_poly.best_degree(x_train=X_train, y_train=Y_train, x_test=X_test, y_test=Y_test, verbose=True)
Y_poly = reg_poly.fit(x_train=X_train, y_train=Y_train).predict(x_test=X)

md.sample_model(sample_data=(X, Y), model_data=(X, Y_poly))

# In[]
# import math
# import pandas as pd

# work_years = float(input("請輸入對方的年資："))
# request_salary = float(input("請輸入對方要求的年薪："))
# salary_pred = reg_poly.predict(pd.DataFrame([[work_years]])).iloc[0, 0]
# salary_lower = reg_poly.predict(pd.DataFrame([[math.floor(work_years)]])).iloc[0, 0]
# salary_upper = reg_poly.predict(pd.DataFrame([[math.ceil(work_years)]])).iloc[0, 0]
# print("合理的月薪推測在 {:.2f} 左右".format(salary_pred))
# print("合理的範圍落在 {:.2f}～{:.2f} 之間".format(salary_lower, salary_upper))

# In[]
from HappyML.performance import rmse

rmse_linear = rmse(Y, Y_simple)
rmse_poly = rmse(Y, Y_poly)

if rmse_linear < rmse_poly:
    print("RMSE Linear:{:.4f} < RMSE Polynomial:{:.4f}...Linear smaller, WIN!!".format(rmse_linear, rmse_poly))
else:
    print("RMSE Linear:{:.4f} > RMSE Polynomial:{:.4f}...Polynomial smaller, WIN!!".format(rmse_linear, rmse_poly))
