import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA

df = pd.read_csv("dataset/Iris/Iris.csv")

print(df.sample(5))
print(df.info())

df['Species'] = pd.factorize(df['Species'])[0]

print(df.sample(5))

print(df.isnull().sum())
df.dropna(inplace=True)

X = df.drop(columns=['Id', 'Species'])
y = df['Species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Without PCA

random_forest_model = RandomForestClassifier(random_state=42)
random_forest_model.fit(X_train, y_train)

y_pred = random_forest_model.predict(X_test)

accuracy_without_pca = accuracy_score(y_test, y_pred)

print("Confusion Matrix without PCA: \n", confusion_matrix(y_test, y_pred))
print("Accuracy without PCA: \n", accuracy_without_pca)

# With PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

X_train_pca, X_test_pca, y_train_pca, y_test_pca = train_test_split(X_pca, y,test_size=0.2, random_state=42)

rf_classifier_pca = RandomForestClassifier(random_state=42)
rf_classifier_pca.fit(X_train_pca, y_train_pca)

y_pred_pca = rf_classifier_pca.predict(X_test_pca)

accuracy_with_pca = accuracy_score(y_test_pca, y_pred_pca)
print("Confusion Matrix:\n", confusion_matrix(y_test_pca, y_pred_pca))
print(f"Accuracy with PCA: {accuracy_with_pca:.2f}")

# 

print(f"Accuracy before PCA: {accuracy_without_pca:.2f}")
print(f"Accuracy after PCA: {accuracy_with_pca:.2f}")


# 

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title('Iris Dataset after PCA')
plt.colorbar()
plt.show()