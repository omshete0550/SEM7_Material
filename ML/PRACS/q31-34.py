import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import seaborn as snb

df = pd.read_csv("dataset/Iris/Iris.csv")

print(df.head())
print(df.info())
print(df.describe())

df['Species'] = pd.factorize(df['Species'])[0]

print(df.isnull().sum())
df.dropna(inplace=True)

X = df.drop(['Id','Species'],axis=1)
y = df['Species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

svm_classifier_rbf = SVC(kernel='rbf')
svm_classifier_rbf.fit(X_train, y_train)

y_pred_rbf = svm_classifier_rbf.predict(X_test)

cm = confusion_matrix(y_test, y_pred_rbf)
print("Confusion Matrix for rbf kernel:\n", cm)

accuracy_rbf = accuracy_score(y_test, y_pred_rbf)
recall_rbf = recall_score(y_test, y_pred_rbf, average='weighted')
precision_rbf = precision_score(y_test, y_pred_rbf, average='weighted')
f1_rbf = f1_score(y_test, y_pred_rbf, average='weighted')


print(f'Accuracy: {accuracy_rbf:.2f}')
print(f'Recall: {recall_rbf:.2f}')
print(f'Precision: {precision_rbf:.2f}')
print(f'F1 Score: {f1_rbf:.2f}')

