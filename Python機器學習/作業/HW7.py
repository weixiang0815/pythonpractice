# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 16:35:04 2021

@author: henry
"""

from sklearn.datasets import load_breast_cancer
import pandas as pd
import HappyML.preprocessor as pp
from HappyML.regression import LogisticRegressor
from HappyML.performance import ClassificationPerformance
import HappyML.model_drawer as md

dataset = load_breast_cancer()

X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
Y = pd.DataFrame(dataset.target, columns=["isBreastCancer"])

selector = pp.KBestSelector()
X = selector.fit(x_ary=X, y_ary=Y, verbose=True, sort=True).transform(x_ary=X)

X_train, X_test, Y_train, Y_test = pp.split_train_test(x_ary=X, y_ary=Y)

X_train, X_test = pp.feature_scaling(fit_ary=X_train, transform_arys=(X_train, X_test))

regressor = LogisticRegressor()
Y_pred = regressor.fit(X_train, Y_train).predict(X_test)

pfm = ClassificationPerformance(Y_test, Y_pred)

print("Confusion Matrix:\n", pfm.confusion_matrix())
print("Accuracy: {:.2%}".format(pfm.accuracy()))
print("Recall: {:.2%}".format(pfm.recall()))
print("Precision: {:.2%}".format(pfm.precision()))
print("F1-score: {:.2%}".format(pfm.f_score()))

selector = pp.KBestSelector(best_k=2)
X = selector.fit(x_ary=X, y_ary=Y, sort=True).transform(x_ary=X)

X_train = selector.transform(X_train)
X_test = selector.transform(X_test)

regressor = LogisticRegressor()
Y_pred = regressor.fit(X_train, Y_train).predict(X_test)

md.classify_result(x=X_train, y=Y_train, classifier=regressor.regressor,
                    title="訓練集樣本點 vs. 模型", font="Microsoft JhengHei")
md.classify_result(x=X_test, y=Y_test, classifier=regressor.regressor,
                    title="測試集樣本點 vs. 模型", font="Microsoft JhengHei")
