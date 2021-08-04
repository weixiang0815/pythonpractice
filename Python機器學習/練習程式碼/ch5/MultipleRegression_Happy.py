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
from HappyML.regression import MultipleRegressor

X_train = pp.add_constant(X_train)
X_test = pp.add_constant(X_test)

regressor = MultipleRegressor()
selected_features = regressor.backward_elimination(x_train=X_train, y_train=Y_train)

Y_predict = regressor.fit(x_train=X_train.iloc[:, selected_features], y_train=Y_train).predict(x_test=X_test.iloc[:, selected_features])

print("Goodness of Model (R-Squared Score):", regressor.r_score())

# In[]
from HappyML.performance import rmse

rmse_linear = rmse(Y_test, Y_pred_simple)
rmse_multi = rmse(Y_test, Y_predict)

if rmse_linear < rmse_multi:
    print("RMSE Linear:{:.4f} < RMSE Multi-Linear:{:.4f}...Linear smaller, WIN!!".format(rmse_linear, rmse_multi))
else:
    print("RMSE Linear:{:.4f} > RMSE Multi-Linear:{:.4f}...Multi-Linear smaller, WIN!!".format(rmse_linear, rmse_multi))

# In[]
from HappyML.criteria import AssumptionChecker

checker = AssumptionChecker(X_train.iloc[:, selected_features], X_test.iloc[:, selected_features], Y_train, Y_test, Y_predict)
checker.y_lim = (-4, 4)
checker.heatmap = True
checker.check_all()
