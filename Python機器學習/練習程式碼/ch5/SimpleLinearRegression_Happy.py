# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:35:29 2021

@author: henry
"""

# In[]
import HappyML.preprocessor as pp

dataset = pp.dataset(file="C:/Users/henry/Desktop/Python Training/Python機器學習/範例原始碼＆「快樂版」函式庫/Ch05 Regression/Salary_Data.csv")

X, Y = pp.decomposition(dataset, [0], [1])

X_train, X_test, Y_train, Y_test = pp.split_train_test(X, Y, train_size=2/3)

X_train, X_test = pp.feature_scaling(X_train, transform_arys=(X_train, X_test))
Y_train, Y_test = pp.feature_scaling(Y_train, transform_arys=(Y_train, Y_test))

# In[]
from HappyML.regression import SimpleRegressor

regressor = SimpleRegressor()
Y_pred= regressor.fit(X_train, Y_train).predict(X_test)

print("R-Squared Score:", regressor.r_score(X_test, Y_test))

# In[]
from HappyML import model_drawer as md

sample_data = (X_train, Y_train)
model_data = (X_train, regressor.predict(X_train))
md.sample_model(sample_data = sample_data, model_data = model_data, title=
                "訓練集樣本點 vs 預測模型", font = "DFKai-sb")
md.sample_model(sample_data = (X_test, Y_test), model_data = (X_test, Y_pred)
                , title="測試集樣本點 vs 預測模型", font = "DFKai-sb")

# In[]
