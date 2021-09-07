# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 20:15:21 2021

@author: henry
"""

# In[]
import HappyML.preprocessor as pp

# Load Dataset
dataset = pp.dataset("C:/Users/henry/Desktop/Python Training/Python機器學習/範例原始碼＆「快樂版」函式庫/Ch10 K-Means/Mall_Customers.csv")

# Decomposition
X = pp.decomposition(dataset, x_columns=[1, 2, 3, 4])

# One-Hot Encoding
X = pp.onehot_encoder(ary=X, columns=[0], remove_trap=True)

# Feature Scaling (for PCA Feature Selection)
X = pp.feature_scaling(fit_ary=X, transform_arys=X)

# Feature Selection (PCA)
from HappyML.preprocessor import PCASelector

selector = PCASelector()
X = selector.fit(x_ary=X, verbose=True, plot=True).transform(x_ary=X)

# In[]
from HappyML.clustering import KMeansCluster

cluster = KMeansCluster()
Y_pred = cluster.fit(x_ary=X, verbose=True, plot=True).predict(x_ary=X, y_column="Customer Type")

# Optional, Attach the Y_pred to Dataset & Save as .CSV file
dataset = pp.combine(dataset, Y_pred)
dataset.to_csv("Mall_Customers_answers.csv", index=False)

# In[]
import HappyML.model_drawer as md

md.cluster_drawer(x=X, y=Y_pred, centroids=cluster.centroids, title="Customers Segmentation")
