import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
# pick features from iris data csv
iris_features_dataset = pd.read_csv("iris.data.csv")
iris_features = np.array(iris_features_dataset)
# using only feature 2 gave highest accuracy score
iris_features = iris_features[:, (2,)]
# pick label from iris target csv
iris_label_dataset = pd.read_csv("iris.target.csv")
b = np.array(iris_label_dataset)
iris_labels = []
for item in b:
    iris_labels.append(item[0])
# use train test split it slice train and test dataset
x_train, x_test, y_train, y_test = train_test_split(iris_features, iris_labels, test_size=0.3, random_state=0)
# print(len(x_test), len(x_train), len(y_test), len(y_train))
# create model object
model = KNeighborsClassifier(n_neighbors=4)
# train the model with train dataset
model.fit(x_train, y_train)
# predict label with test dataset
y_predict = model.predict(x_test)
print(f"Y Predict     : {y_predict}")
print(f"Y Test        : {np.array(y_test)}")
# print accuracy of the model, confusion matrix and classification report
print(f"Accuracy Score: {round(accuracy_score(np.array(y_test),y_predict)*100)}")
con_matrix = confusion_matrix(y_test, y_predict)
print(f"Confusion matrix: \n{con_matrix}")
print(f"Classification Report: \n{classification_report(y_test, y_predict)}")
# plot confusion matrix on a heatmap
sns.heatmap(con_matrix, annot=True)
plt.legend()
plt.xlabel("Actual Value")
plt.ylabel("Predicted Value")
plt.title("Confusion Matrix")
plt.show()
# Features:
# sepal length in cm
# sepal width in cm
# petal length in cm
# petal width in cm
# class (Labels):
# Iris Setosa      --> 0
# Iris Versicolour --> 1
# Iris Virginica   --> 2
