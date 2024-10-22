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

svm_classifier_linear = SVC(kernel='linear')
svm_classifier_linear.fit(X_train, y_train)

y_pred_linear = svm_classifier_linear.predict(X_test)

cm = confusion_matrix(y_test, y_pred_linear)
print("Confusion Matrix for linear kernel:\n", cm)

accuracy_linear = accuracy_score(y_test, y_pred_linear)
recall_linear = recall_score(y_test, y_pred_linear, average='weighted')
precision_linear = precision_score(y_test, y_pred_linear, average='weighted')
f1_linear = f1_score(y_test, y_pred_linear, average='weighted')

print(f'Accuracy: {accuracy_linear:.2f}')
print(f'Recall: {recall_linear:.2f}')
print(f'Precision: {precision_linear:.2f}')
print(f'F1 Score: {f1_linear:.2f}')
