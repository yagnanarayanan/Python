"""
Get the lowest MSE using individual features or combination of features with Linear Regression Model using iris dataset
"""
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# read the CSV for features dataset and convert to np array
iris_data = pd.read_csv("iris.data.csv")
iris_features = np.array(iris_data)
# choose the features you want to use to train the model
iris_features = iris_features[:, (2, 3)]
# read the csv for label dataset and convert to numpy array
iris_target_read = pd.read_csv("iris.target.csv")
b = np.array(iris_target_read)
c = []
for item in b:
    c.append(item[0])
iris_label = np.array(c)
# create object for linear regression model
model = linear_model.LinearRegression()
# split the data as test and train.
# Test size 0.3 means 30% of the data set is for testing the model. random state is for same random split each time
x_train, x_test, y_train, y_test = train_test_split(iris_features, iris_label, test_size=0.3, random_state=0)
# train the model
model.fit(x_train, y_train)
# predict label using the test dataset
y_predict = model.predict(x_test)
# used rounding the converting to int as model output was in float
print(f"y_predict: {np.round(y_predict).astype(int)}")
# print(f"y_predict: {y_predict}")
print(f"y_test   : {y_test}")
# print MSE, weights and intercept
print(f"Mean squared error of model: {mean_squared_error(np.round(y_predict).astype(int), y_test)}")
print(f"Model weights: {model.coef_}")
print(f"Model intercept: {model.intercept_}")
# below plotting will work only for single feature training
# plt.scatter(x_test, y_test)
# plt.plot(x_test, y_predict)
# plt.show()

# Observations with 30% test size:
# MSE using all features: 0.08888888888888889
# MSE using index 0 (f1): 0.3111111111111111
# MSE using index 1 (f2): 0.7111111111111111
# MSE using index 2 (f3): 0.022222222222222223
# MSE using index 3 (f4): 0.08888888888888889
# MSE using index 2,3 (f3,f4): 0.1111111111111111
# where
# f1: sepal length in cm
# f2: sepal width in cm
# f3: petal length in cm
# f4: petal width in cm
