# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 08:06:43 2021

@author: henry
"""

import HappyML.preprocessor as pp
from HappyML.classification import RandomForest
from HappyML.performance import KFoldClassificationPerformance
from random import randint
import HappyML.model_drawer as md
from IPython.display import Image, display

dataset = pp.dataset("Zoo_Data.csv")
dataset_classname = pp.dataset("Zoo_Class_Name.csv")
class_names = [row["Class_Type"] for index, row in dataset_classname.iterrows()]

X, Y = pp.decomposition(dataset, [i for i in range(17) if i != 0], [17])

selector = pp.KBestSelector(best_k="auto")
X = selector.fit(X, Y, sort=False).transform(X)

X_train, X_test, Y_train, Y_test = pp.split_train_test(X, Y)

classifier = RandomForest()
Y_pred = classifier.fit(X_train, Y_train).predict(X_test)

kfp = KFoldClassificationPerformance(X, Y, classifier.classifier)

print("Using KBest:")
print("----- Random Forest Classification -----")
print("{} Folds Mean Accuracy: {}".format(10, kfp.accuracy()))
print("{} Folds Mean Recall: {}".format(10, kfp.recall()))
print("{} Folds Mean Precision: {}".format(10, kfp.precision()))
print("{} Folds Mean F1-Score: {}".format(10, kfp.f_score()))

GRAPHVIZ_INSTALL = "C:/Program Files (x86)/Graphviz/bin"

clfr = classifier.classifier.estimators_[randint(0, len(classifier.classifier.estimators_)-1)]
graph = md.tree_drawer(clfr, X_test.columns, class_names, GRAPHVIZ_INSTALL)
display(Image(graph.create_png()))
