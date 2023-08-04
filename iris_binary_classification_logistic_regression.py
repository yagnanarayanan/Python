# Binary Classification of Iris Virginica using Logistic Regression. Plotting confusion matrix and S-Curve
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt
iris = datasets.load_iris()
# print(iris.DESCR)
iris_features = iris.data[:, (2,)]
# print(iris_features)
# the idea here is to perform binary classification based on features if it's an Iris Virginica or not.
iris_label = (iris.target == 2).astype(int)
iris_label = np.array(iris_label)
x_train, x_test, y_train, y_test = train_test_split(iris_features, iris_label, test_size=0.3, random_state=0)
# print(len(x_test), len(x_train), len(y_test), len(y_train))
model = LogisticRegression()
model.fit(x_train, y_train)
y_predict = model.predict(x_test)
print(f"Y Test   : {y_test}")
print(f"Y Predict: {y_predict}")
con_matrix = confusion_matrix(y_test, y_predict)
print("Classification Report:")
print(classification_report(y_test, y_predict))
print("Confusion Matrix:")
print(con_matrix)
print("Accuracy Score:")
print(accuracy_score(y_test, y_predict))
# print(model.predict_proba(x_test))
# plot Confusion Matrix
sns.heatmap(con_matrix, annot=True)
plt.xlabel("Actual Value")
plt.ylabel("Predicted Value")
plt.title("Confusion Matrix")
plt.show()
# plotting S-Curve graph for 1500 single feature points
X_new = np.linspace(0, 8, 1500).reshape(-1, 1)
Y_predict = model.predict_proba(X_new)
plt.plot(X_new, Y_predict[:, 1])
plt.xlabel("Petal length in cm")
plt.ylabel("Probability of Iris Virginica")
plt.show()
