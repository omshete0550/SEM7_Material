#37. The Iris data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant.
# i. Understand the Dataset & cleanup (if required).
# ii. Build a decision tree classifier to predict the iris plant category? (Use log loss criteria, use
# max_depth=4, min_samples_split=2)
# iii. Evaluate the model using Accuracy. 

import pandas as pd
import seaborn as snb
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, log_loss

df = pd.read_csv("dataset/Iris/Iris.csv")

print(df.sample(5))
print(df.info())

df['Species'] = pd.factorize(df['Species'])[0]

print(df.isnull().sum())

df.dropna(inplace=True)

X = df.drop(['Id', 'Species'], axis=1)
y = df['Species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

dt_classifier = DecisionTreeClassifier(criterion="log_loss", max_depth=4, min_samples_split=2, random_state=42)
dt_classifier.fit(X_train, y_train)

y_pred = dt_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy Score: {accuracy}")

plt.figure(figsize=(12,8))
plot_tree(dt_classifier, filled=True, feature_names=X.columns, class_names=["Iris-setosa","Iris-versicolor","Iris-virginica"], rounded=True)
plt.title("Decision Tree Visualization")
plt.show()