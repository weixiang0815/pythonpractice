# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 05:49:05 2021

@author: henry
"""

import HappyML.preprocessor as pp
from HappyML.classification import DecisionTree
from HappyML.performance import KFoldClassificationPerformance
import HappyML.model_drawer as md
from IPython.display import Image, display

dataset = pp.dataset("HR-Employee-Attrition.csv")

X, Y = pp.decomposition(dataset, [i for i in range(35) if i != 1], [1])
X = pp.onehot_encoder(X, [1, 3, 6, 10, 14, 16, 20, 21], True)
Y, Y_mapping = pp.label_encoder(Y, True)

selector = pp.KBestSelector()
X = selector.fit(X, Y, True, True).transform(X)

X_train, X_test, Y_train, Y_test = pp.split_train_test(X, Y)

classifier = DecisionTree()
Y_pred = classifier.fit(X_train, Y_train).predict(X_test)

K = 10
kfp = KFoldClassificationPerformance(X, Y, classifier.classifier, K)

print("----- Decision Tree Classification -----")
print("{} Folds Mean Accuracy: {}".format(K, kfp.accuracy()))
print("{} Folds Mean Recall: {}".format(K, kfp.recall()))
print("{} Folds Mean Precision: {}".format(K, kfp.precision()))
print("{} Folds Mean F1-Score: {}".format(K, kfp.f_score()))

GRAPHVIZ_INSTALL = "C:/Program Files (x86)/Graphviz/bin"

cls_name = [Y_mapping[key] for key in sorted(Y_mapping.keys())]
graph = md.tree_drawer(classifier.classifier, X_test.columns, cls_name, GRAPHVIZ_INSTALL)
display(Image(graph.create_png()))

# 根據決策樹，員工留/離職最重要的原因是加班與否(OverTime_Yes)
