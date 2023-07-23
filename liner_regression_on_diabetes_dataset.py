import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error
# load the dataset diabetes
diabetes_dataset = datasets.load_diabetes()
# show keys in the dataset
# print(diabetes_dataset.keys())
# dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])
# show data from the dataset
# print(diabetes_dataset.data)
# describe the dataset
# print(diabetes_dataset.DESCR)
# use only the 3rd column (index position 2) as independent variable to predict the dependent variable
# if you want to use all available features (independent variables) don't give anything after .data in below line
diabetes_X = diabetes_dataset.data[:, np.newaxis, 2]
# new axis is a convenient alias for None, useful for indexing arrays
# slice the data into training and testing as per your choice. More training data, the better
# first slice for X
diabetes_X_train = diabetes_X[:300]
diabetes_X_test = diabetes_X[300:350]
# then sice for Y
diabetes_Y_train = diabetes_dataset.target[:300]
diabetes_Y_test = diabetes_dataset.target[300:350]
# create object 'model' for linear regression
model = linear_model.LinearRegression()
# fit the trained dataset into the model
model.fit(diabetes_X_train, diabetes_Y_train)
# predict Y for the test X sliced data
diabetes_Y_predict = model.predict(diabetes_X_test)
# print the mean squared error, weights and intercepts
print(f"Mean Squared error is {mean_squared_error(diabetes_Y_test,diabetes_Y_predict)}")
print(f"Weights: {model.coef_}")
print(f"Intercept: {model.intercept_}")
# plot the test data (X and Y) and draw the line for predicted Y
plt.scatter(diabetes_X_test, diabetes_Y_test)
plt.plot(diabetes_X_test, diabetes_Y_predict)
plt.show()
