# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 00:22:54 2021

@author: henry
"""

import HappyML.preprocessor as pp
from HappyML.classification import SVM
from HappyML.performance import KFoldClassificationPerformance
import numpy as np
from HappyML.performance import GridSearch

# SVM without GridSearch
dataset = pp.dataset("Voice.csv")
X, Y = pp.decomposition(dataset, [i for i in range(20)], [20])
Y, Y_mapping = pp.label_encoder(Y, mapping=True)

selector = pp.KBestSelector()
X = selector.fit(X, Y, True, True).transform(X)

X_train, X_test, Y_train, Y_test = pp.split_train_test(X, Y)
X_train, X_test = pp.feature_scaling(X_train, (X_train, X_test))

classifier = SVM()
Y_pred = classifier.fit(X_train, Y_train).predict(X_test)

K = 10
kfp = KFoldClassificationPerformance(X, Y, classifier.classifier, K)

print("----- SVM Classification -----")
print("{} Folds Mean Accuracy: {}".format(K, kfp.accuracy()))
print("{} Folds Mean Recall: {}".format(K, kfp.recall()))
print("{} Folds Mean Precision: {}".format(K, kfp.precision()))
print("{} Folds Mean F1-score: {}".format(K, kfp.f_score()))

# SVM with GridSearch
X, Y = pp.decomposition(dataset, [i for i in range(20)], [20])
Y, Y_mapping = pp.label_encoder(Y, mapping=True)

selector = pp.KBestSelector()
X = selector.fit(X, Y, True, True).transform(X)

X_train, X_test, Y_train, Y_test = pp.split_train_test(X, Y)
X_train, X_test = pp.feature_scaling(X_train, (X_train, X_test))

C_range = np.logspace(3, 6, 4)
Gamma_range = np.logspace(-4, -1, 4)
Coef0_range = np.logspace(0, 3, 4)

Linear_dict = dict(kernel=["linear"], C=C_range, coef0=Coef0_range)
RBF_dict = dict(kernel=["rbf"], C=C_range, gamma=Gamma_range)
Sigmoid_dict = dict(kernel=["sigmoid"], C=C_range, gamma=Gamma_range, coef0=Coef0_range)

params_list = [Linear_dict, RBF_dict, Sigmoid_dict]

classifier = SVM()

validator = GridSearch(estimator=classifier.classifier, parameters=params_list)
validator.fit(X, Y)
print("Best Parameters: {}　Best Score: {}".format(validator.best_params_, validator.best_score_))
classifier.classifier = validator.best_estimator_

Y_pred = classifier.fit(X_train, Y_train).predict(X_test)

kfp = KFoldClassificationPerformance(X, Y, classifier.classifier, K)

print("----- SVM Classification -----")
print("{} Folds Mean Accuracy: {}".format(K, kfp.accuracy()))
print("{} Folds Mean Recall: {}".format(K, kfp.recall()))
print("{} Folds Mean Precision: {}".format(K, kfp.precision()))
print("{} Folds Mean F1-score: {}".format(K, kfp.f_score()))
