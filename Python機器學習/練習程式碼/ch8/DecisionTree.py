# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 20:11:45 2021

@author: henry
"""

# In[]
import HappyML.preprocessor as pp

dataset = pp.dataset(file="Mushrooms.csv")

X, Y = pp.decomposition(dataset, x_columns=[i for i in range(1, 23)], y_columns=[0])

X = pp.onehot_encoder(X, columns=[i for i in range(22)], remove_trap=True)
Y, Y_mapping = pp.label_encoder(Y, mapping=True)

from HappyML.preprocessor import KBestSelector
selector = KBestSelector(best_k="auto")
X = selector.fit(x_ary=X, y_ary=Y, verbose=True, sort=True).transform(x_ary=X)

X_train, X_test, Y_train, Y_test = pp.split_train_test(x_ary=X, y_ary=Y)

# In[]
from HappyML.classification import DecisionTree

classifier = DecisionTree()
Y_pred = classifier.fit(X_train, Y_train).predict(X_test)

# In[]
from HappyML.performance import KFoldClassificationPerformance

K = 10
kfp = KFoldClassificationPerformance(x_ary=X, y_ary=Y, classifier=classifier.classifier, k_fold=K)

print("----- Decision Tree Classification -----")
print("{} Folds Mean Accuracy: {}".format(K, kfp.accuracy()))
print("{} Folds Mean Recall: {}".format(K, kfp.recall()))
print("{} Folds Mean Precision: {}".format(K, kfp.precision()))
print("{} Folds Mean F1-Score: {}".format(K, kfp.f_score()))

# In[]
GRAPHVIZ_INSTALL = "C:/Program Files (x86)/Graphviz/bin"

import HappyML.model_drawer as md
from IPython.display import Image, display

cls_name = [Y_mapping[key] for key in sorted(Y_mapping.keys())]
graph = md.tree_drawer(classifier=classifier.classifier, feature_names=X_test.columns, target_names=cls_name, graphviz_bin=GRAPHVIZ_INSTALL)
display(Image(graph.create_png()))