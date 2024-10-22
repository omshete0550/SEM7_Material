import pandas as pd
import matplotlib.pyplot as plt
import seaborn as snb
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score

df = pd.read_csv("dataset/Social_Network_Ads/Social_Network_Ads.csv")

print(df.head())
print(df.info())
print(df.describe())

print(df.isnull().sum())

df.dropna(inplace=True)

plt.figure(figsize=(10, 6))
snb.scatterplot(data=df, x='EstimatedSalary', y='Age', hue='Purchased', palette='viridis', alpha=0.7)
plt.title('Scatter Plot of Age vs Estimated Salary')
plt.xlabel('Estimated Salary')
plt.ylabel('Age')
plt.legend(title='Purchased', loc='upper left', labels=['No', 'Yes'])
plt.show()

# Encoding categorical data
df['Gender'] = pd.factorize(df['Gender'])[0] # Male=0, Female=1
# Features and target variable
X = df[['Gender', 'Age', 'EstimatedSalary']]
y = df['Purchased']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the SVM model
svm_classifier_linear = SVC(kernel='linear')
svm_classifier_linear.fit(X_train, y_train)

y_pred_linear = svm_classifier_linear.predict(X_test)

# confusion matrix
cm = confusion_matrix(y_test, y_pred_linear)
print("Confusion Matrix for linear kernel:\n", cm)

# metrics
accuracy_linear = accuracy_score(y_test, y_pred_linear)
recall_linear = recall_score(y_test, y_pred_linear)
precision_linear = precision_score(y_test, y_pred_linear)
f1_linear = f1_score(y_test, y_pred_linear)

print("For linear kernel")
print(f'Accuracy: {accuracy_linear:.2f}')
print(f'Recall: {recall_linear:.2f}')
print(f'Precision: {precision_linear:.2f}')
print(f'F1 Score: {f1_linear:.2f}')
