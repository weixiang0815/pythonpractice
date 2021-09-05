# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 21:53:40 2021

@author: henry
"""

import HappyML.preprocessor as pp
from HappyML.regression import PolynomialRegressor
import pandas as pd
import HappyML.model_drawer as md
from HappyML.performance import rmse

dataset = pp.dataset("Device_Failure.csv")
X, Y = pp.decomposition(dataset, x_columns=[0], y_columns=[1])

X_train, X_test, Y_train, Y_test = pp.split_train_test(x_ary=X, y_ary=Y, train_size=0.75)

reg_poly = PolynomialRegressor()
reg_poly.best_degree(x_train=X_train, y_train=Y_train, x_test=X_test, y_test=Y_test)
Y_poly = reg_poly.fit(x_train=X, y_train=Y).predict(x_test=X)

years = float(input("請輸入設備已使用年份："))
hours_pred = reg_poly.predict(pd.DataFrame([[years]])).iloc[0, 0]
print("您的設備預測總失效時間 =", "{:.4f}".format(hours_pred), "小時")
print("平均每年失效時間 =", "{:.4f}".format(hours_pred/years), "小時/年")

md.sample_model(sample_data=(X, Y), model_data=(X, Y_poly))
print("Degree =", reg_poly.degree, "RMSE =", "{:.4f}".format(rmse(Y, Y_poly)))
