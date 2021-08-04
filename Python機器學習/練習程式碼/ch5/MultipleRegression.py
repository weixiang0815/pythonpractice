# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 18:25:36 2021

@author: henry
"""

# In[]
import HappyML.preprocessor as pp

dataset = pp.dataset("C:/Users/henry/Desktop/Python Training/Python機器學習/範例原始碼＆「快樂版」函式庫/Ch05 Regression/50_Startups.csv")
X, Y = pp.decomposition(dataset, [0, 1, 2, 3], [4])

# X = pp.onehot_encoder(X, columns=[3])
# X = pp.remove_columns(X, [3])

X = pp.onehot_encoder(X, columns=[3], remove_trap=True)

X_train, X_test, Y_train, Y_test = pp.split_train_test(X, Y, train_size=0.8)

X_train, X_test= pp.feature_scaling(fit_ary=X_train, transform_arys=(X_train, X_test))
Y_train, Y_test= pp.feature_scaling(fit_ary=Y_train, transform_arys=(Y_train, Y_test))

# In[]
from HappyML.regression import SimpleRegressor

simple_reg = SimpleRegressor()
Y_pred_simple = simple_reg.fit(X_train, Y_train).predict(X_test)

# R-Squared always increase in multiple linear regression --> Use Adjusted R-Squared instead
print("Goodness of Model (R-Squared Score):", simple_reg.r_score(X_test, Y_test))

# In[]
import statsmodels.tools.tools as smtools
X_train = smtools.add_constant(X_train)

# In[]
import statsmodels.api as sm
features = [0, 1, 3]
X_opt = X_train.iloc[:, features]

regressor_OLS = sm.OLS(exog=X_opt, endog=Y_train).fit()
print(regressor_OLS.summary())

# In[]
X_test = smtools.add_constant(X_test)

X_opttest = X_test.iloc[:, features]
Y_predmulti = regressor_OLS.predict(X_opttest)

# In[]
from sklearn.metrics import mean_squared_error
import numpy as np

rmse_linear = np.sqrt(mean_squared_error(Y_test, Y_pred_simple))
rmse_multi = np.sqrt(mean_squared_error(Y_test, Y_predmulti))

if rmse_linear < rmse_multi:
    print("RMSE Linear:{:.4f} < RMSE Multi-Linear:{:.4f}...Linear smaller, WIN!!".format(rmse_linear, rmse_multi))
else:
    print("RMSE Linear:{:.4f} > RMSE Multi-Linear:{:.4f}...Multi-Linear smaller, WIN!!".format(rmse_linear, rmse_multi))

# In[]
from HappyML.criteria import AssumptionChecker

checker = AssumptionChecker(X_train.iloc[:, features], X_test.iloc[:, features], Y_train, Y_test, Y_predmulti)
checker.y_lim = (-4, 4)
checker.heatmap = True
checker.check_all()
