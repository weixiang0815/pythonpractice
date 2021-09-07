# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 09:06:38 2021

@author: henry
"""

import HappyML.preprocessor as pp
from HappyML.clustering import KMeansCluster
import HappyML.model_drawer as md
from HappyML.classification import DecisionTree
from HappyML.performance import KFoldClassificationPerformance
from IPython.display import Image, display

dataset = pp.dataset("CreditCards.csv")

dataset = pp.missing_data(dataset)

X = pp.decomposition(dataset, [i for i in range(18) if i != 0])

X = pp.feature_scaling(X, X)

selector = pp.PCASelector(best_k=2)
X = selector.fit(X).transform(X)

cluster = KMeansCluster()
Y_pred = cluster.fit(X).predict(X, "Customer Type")

md.cluster_drawer(X, Y_pred, cluster.centroids, "Customers Segmentation", "Microsoft JhengHei")

dataset = pp.combine(dataset, Y_pred)

X, Y = pp.decomposition(dataset, [i for i in range(18) if i != 0], [18])

selector = pp.KBestSelector()
X = selector.fit(X, Y).transform(X)

X_train, X_test, Y_train, Y_test = pp.split_train_test(X, Y)

classifier = DecisionTree()
Y_pred = classifier.fit(X_train, Y_train).predict(X_test)

kfp = KFoldClassificationPerformance(X, Y, classifier.classifier)

print("----- Decision Tree Classification -----")
print("10 Folds Mean Accuracy: {}".format(kfp.accuracy()))
print("10 Folds Mean Recall: {}".format(kfp.recall()))
print("10 Folds Mean Precision: {}".format(kfp.precision()))
print("10 Folds Mean F1_Score: {}".format(kfp.f_score()))

GRAPHVIZ_INSTALL = "C:/Program Files (x86)/Graphviz/bin"

graph = md.tree_drawer(classifier.classifier, X.columns, "0123", GRAPHVIZ_INSTALL)
display(Image(graph.create_png()))
# 從繪製出的決策樹得知，該集群結果最重要的決定因素為購物頻率(Purchase Frequency)
