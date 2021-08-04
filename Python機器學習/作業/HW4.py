# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 11:40:29 2021

@author: henry
"""

from HappyML import preprocessor as pp
from HappyML.regression import SimpleRegressor
import pandas as pd
from HappyML import model_drawer as md

dataset_h = pp.dataset("Student_Height.csv")
dataset_w = pp.dataset("Student_Weight.csv")

X_h, Y_h = pp.decomposition(dataset_h, [1], [3, 4])
X_w, Y_w = pp.decomposition(dataset_w, [1], [3, 4])

X_h_train, X_h_test, Y_h_train, Y_h_test = pp.split_train_test(X_h, Y_h)
X_w_train, X_w_test, Y_w_train, Y_w_test = pp.split_train_test(X_w, Y_w)

regressor = [[SimpleRegressor(), SimpleRegressor()], [SimpleRegressor(), SimpleRegressor()]]
regressor[0][0].fit(X_h_train, Y_h_train.iloc[:, 0].to_frame())
regressor[0][1].fit(X_h_train, Y_h_train.iloc[:, 1].to_frame())
regressor[1][0].fit(X_w_train, Y_w_train.iloc[:, 0].to_frame())
regressor[1][1].fit(X_w_train, Y_w_train.iloc[:, 1].to_frame())

print("台灣 6~15 歲學童身高、體重評估系統\n")
gender = eval(input("請輸入您的性別（1.男 2.女）：")) -1
age = eval(input("請輸入您的年齡（6-15）："))
height = eval(input("請輸入您的身高（cm）："))
weight = eval(input("請輸入您的體重（kg）："))

h_avg = regressor[0][gender].predict(x_test=pd.DataFrame([[age]])).iloc[0, 0]
w_avg = regressor[1][gender].predict(x_test=pd.DataFrame([[age]])).iloc[0, 0]

model_data_h = (X_h_train, regressor[0][gender].predict(X_h_train))
md.sample_model(sample_data=(age, height), model_data=model_data_h,
                title="身高落點分布", xlabel="年齡", ylabel="身高",
                font="Microsoft JhengHei")
if gender == 0:
    print(age, "歲男生平均身高為", "{:.2f}".format(h_avg), "公分，您的身高為", height, "公分")
elif gender == 1:
    print(age, "歲女生平均身高為", "{:.2f}".format(h_avg), "公分，您的身高為", height, "公分")

model_data_w = (X_w_train, regressor[1][gender].predict(X_w_train))
md.sample_model(sample_data=(age, weight), model_data=model_data_w,
                title="體重落點分布", xlabel="年齡", ylabel="體重",
                font="Microsoft JhengHei")
if gender == 0:
    print(age, "歲男生平均體重為", "{:.2f}".format(w_avg), "公斤，您的體重為", weight, "公斤")
elif gender == 1:
    print(age, "歲女生平均體重為", "{:.2f}".format(w_avg), "公斤，您的體重為", weight, "公斤")