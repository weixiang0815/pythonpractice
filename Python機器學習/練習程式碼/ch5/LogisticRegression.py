# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 19:22:57 2021

@author: henry
"""

# In[]
import HappyML.preprocessor as pp

dataset = pp.dataset(file="C:/Users/henry/Desktop/Python Training/Python機器學習/範例原始碼＆「快樂版」函式庫/Ch05 Regression/Social_Network_Ads.csv")

X, Y = pp.decomposition(dataset, x_columns=[1, 2, 3], y_columns=[4])

X = pp.onehot_encoder(X, columns=[0], remove_trap=True)

X_train, X_test, Y_train, Y_test = pp.split_train_test(X, Y)

X_train, X_test = pp.feature_scaling(fit_ary=X_train, transform_arys=(X_train, X_test))

# In[]
from sklearn.linear_model import LogisticRegression
import time

classifier = LogisticRegression(solver="lbfgs", random_state=int(time.time()))

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

kbest = SelectKBest(score_func=chi2, k=2)
kbest = kbest.fit(X, Y)
print("The p-values of Feature Importance: {}".format(kbest.pvalues_))

X_train = kbest.transform(X_train)
X_test = kbest.transform(X_test)

classifier.fit(X_train, Y_train.values.ravel())

Y_pred_logistic = classifier.predict(X_test)

# In[]
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import fbeta_score

print("Confusion Matrix:\n", confusion_matrix(y_true=Y_test, y_pred=Y_pred_logistic))
print("Accuracy: {:.2%}".format(accuracy_score(Y_test, Y_pred_logistic)))
print("Recall: {:.2%}".format(recall_score(Y_test, Y_pred_logistic)))
print("Precision: {:.2%}".format(precision_score(Y_test, Y_pred_logistic)))
print("F1-score: {:.2%}".format(fbeta_score(Y_test, Y_pred_logistic, beta=1)))
