# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 18:53:16 2021

@author: henry
"""

import numpy as np
from scipy.spatial.distance import pdist, squareform

# Define 3 points
x = np.array([[0, 1], [1, 0], [2, 0]])

# Calculate Eclidean Distance
x = pdist(x, "euclidean")

# Show in Cross Table Form
print(squareform(x))
