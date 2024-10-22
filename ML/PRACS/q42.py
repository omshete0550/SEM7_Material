# 42. The Iris data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant.
# i. Understand the Dataset & cleanup (if required).
# ii. Build a AdaBoost Classifier model to predict the iris plant category?
# iii. Evaluate the model using Accuracy

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("dataset/Iris/Iris.csv")

print(df.sample(5))
print(df.info())

df['Species'] = pd.factorize(df['Species'])[0]
print(df.head())

print(df.isnull().sum())
df.dropna(inplace=True)

print(df['Species'].value_counts())

X = df.drop(columns=['Id', 'Species'])
y = df['Species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

ada_boost_model = AdaBoostClassifier()
ada_boost_model.fit(X_train, y_train)

y_pred = ada_boost_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Ada Boost Classifier Accuracy: {accuracy:.2f}")
