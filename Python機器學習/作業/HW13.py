# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 09:57:19 2021

@author: henry
"""

import HappyML.preprocessor as pp
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import pandas as pd
from HappyML.performance import ClassificationPerformance

dataset = pp.dataset("Churn_Modelling.csv")

X, Y = pp.decomposition(dataset, [i for i in range(3, 13)], [13])

X = pp.onehot_encoder(X, [1, 2], True)

selector = pp.KBestSelector()
X = selector.fit(X, Y, True, True).transform(X)

X_train, X_test, Y_train, Y_test = pp.split_train_test(X, Y)

X_train, X_test = pp.feature_scaling(X_train, (X_train, X_test))

classifier = Sequential()

arithmetic_mean = [0, 0]
arithmetic_mean[0] = int((X_train.shape[1]+1)/2)
arithmetic_mean[1] = int((arithmetic_mean[0]+1)/2)

experience_law = [0, 0]
alpha = 5
experience_law[0] = int(X_train.shape[0]/(alpha*(X_train.shape[1]+1)))
experience_law[1] = int(X_train.shape[0]/(alpha*(experience_law[0]+1)))

classifier.add(Dense(input_dim=X_train.shape[1], units=experience_law[0], kernel_initializer="random_normal", activation="relu"))
classifier.add(Dense(units=experience_law[1], kernel_initializer="random_normal", activation="relu"))
classifier.add(Dense(units=1, kernel_initializer="random_normal", activation="sigmoid"))

classifier.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

classifier.fit(x=X_train, y=Y_train, batch_size=10, epochs=100)
print()

Y_pred = classifier.predict(X_test).astype(int)
Y_pred = pd.DataFrame(Y_pred, Y_test.index, Y_test.columns)

pfm = ClassificationPerformance(Y_test, Y_pred)

print("Confusion Matrix:\n", pfm.confusion_matrix())
print("Accuracy: {:.2%}".format(pfm.accuracy()))
print("Recall: {:.2%}".format(pfm.recall()))
print("Precision: {:.2%}".format(pfm.precision()))
print("F1-score: {:.2%}".format(pfm.f_score()))
