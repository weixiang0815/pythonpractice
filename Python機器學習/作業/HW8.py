# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 16:35:04 2021

@author: henry
"""

import HappyML.preprocessor as pp
from HappyML.classification import NaiveBayesClassifier
from HappyML.performance import KFoldClassificationPerformance
from HappyML.criteria import AssumptionChecker
import HappyML.model_drawer as md

dataset = pp.dataset("Diabetes.csv")
X, Y = pp.decomposition(dataset, x_columns=[i for i in range(8)], y_columns=[-1])

selector = pp.KBestSelector()
X = selector.fit(x_ary=X, y_ary=Y, verbose=True, sort=True).transform(x_ary=X)

X_train, X_test, Y_train, Y_test = pp.split_train_test(x_ary=X, y_ary=Y)

X_train, X_test = pp.feature_scaling(fit_ary=X_train, transform_arys=(X_train, X_test))

classifier = NaiveBayesClassifier()
Y_pred = classifier.fit(X_train, Y_train).predict(X_test)

K = 10
Kfp = KFoldClassificationPerformance(X, Y, classifier.classifier, K)

print("{} Folds Mean Accuracy: {}".format(K, Kfp.accuracy()))
print("{} Folds Mean Recall: {}".format(K, Kfp.recall()))
print("{} Folds Mean Precision: {}".format(K, Kfp.precision()))
print("{} Folds Mean F1-Score: {}".format(K, Kfp.f_score()))

checker = AssumptionChecker(X_train, X_test, Y_train, Y_test, Y_pred)
checker.features_correlation()

selector = pp.KBestSelector(best_k=2)
X = selector.fit(X, Y, False, True).transform(X)

X_train = selector.transform(X_train)
X_test = selector.transform(X_test)

X_train, X_test = pp.feature_scaling(fit_ary=X_train, transform_arys=(X_train, X_test))

classifier = NaiveBayesClassifier()
Y_pred = classifier.fit(X_train, Y_train).predict(X_test)

md.classify_result(x=X_train, y=Y_train, classifier=classifier, title="訓練集 vs. 模型", font="Microsoft JhengHei")
md.classify_result(x=X_test, y=Y_test, classifier=classifier, title="測試集 vs. 模型", font="Microsoft JhengHei")
