import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix, accuracy_score

# Load Dataset
df = pd.read_csv("dataset/Iris/Iris.csv")

# Understanding the dataset
print(df.head())
print(df.info())
print(df.describe())

# Check for missing values
print(df.isnull().sum())
df.dropna(inplace=True)

# Model without PCA

X = df.drop(columns=['Id', 'Species'])
y = df['Species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rfc_model = RandomForestClassifier(random_state=42)
rfc_model.fit(X_train, y_train)

y_pred_rfc = rfc_model.predict(X_test)

cm = confusion_matrix(y_test, y_pred_rfc)
print("Confusion matrix withou PCA: \n", cm)

accuracy_rfc = accuracy_score(y_test, y_pred_rfc)
print("Confusion matrix withou PCA: \n", accuracy_rfc)

# Model with PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

X_train_pca, X_test_pca, y_train_pca, y_test_pca = train_test_split(X_pca, y, test_size=0.2, random_state=42)

rfc_model_pca = RandomForestClassifier(random_state=42)
rfc_model_pca.fit(X_train_pca, y_train_pca)

y_pred_pca = rfc_model_pca.predict(X_test_pca)

cm_pca = confusion_matrix(y_test_pca, y_pred_pca)
print("Confusion matrix with PCA: \n", cm_pca)

accuracy_pca = accuracy_score(y_test_pca, y_pred_pca)
print("Confusion matrix with PCA: \n", accuracy_pca)

