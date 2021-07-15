# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 20:29:48 2021

@author: henry
"""

import matplotlib.pyplot as plt
import numpy as np

# In[]
X = np.arange(0., 5., 0.2)
plt.plot(X, X, "r--")
plt.plot(X, X**2, "bs")
plt.plot(X, X**3, "g^")
plt.show()

# In[]
