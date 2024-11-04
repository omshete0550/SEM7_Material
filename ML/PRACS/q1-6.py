import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from LinearRegression import LinearRegression 
from sklearn.metrics import mean_squared_error

# load dataset
df = pd.read_csv("dataset/advertising/advertising.csv")

# i. Understand the Dataset & cleanup (if required).
print("\nSample Data: \n", df.head())

# data info
print("Data Info: \n")
df.info()

# describe data
print("\nData Description: \n", df.describe())

# check for missing data
print("\nMissing Values: \n", df.isnull().sum())

# if data consists missing data
df = df.dropna(subset=["TV Ad Budget ($)",	"Radio Ad Budget ($)", 	"Newspaper Ad Budget ($)",	"Sales ($)"])

# Visualize data
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Radio Ad Budget ($)", y="Sales ($)")
plt.show()

# sales w.r.t Radio features.
X1 = df[['Radio Ad Budget ($)']]
y1 = df['Sales ($)']

# sales w.r.t attribute tv.
X2 = df[['TV Ad Budget ($)']]
y2 = df['Sales ($)']

# sales w.r.t attribute newspaper.
X3 = df[['Newspaper Ad Budget ($)']]
y3 = df['Sales ($)']

# sales w.r.t Radio and TV
X4 = df[['Radio Ad Budget ($)', 'TV Ad Budget ($)']]
y4 = df['Sales ($)']

# sales w.r.t Newspaper and TV
X5 = df[['Newspaper Ad Budget ($)', 'TV Ad Budget ($)']]
y5 = df['Sales ($)']

# sales w.r.t Newspaper and Radio
X6 = df[['Newspaper Ad Budget ($)', 'Radio Ad Budget ($)']]
y6 = df['Sales ($)']

X_train, X_test, y_train, y_test = train_test_split(X2, y2, test_size=0.2, random_state=42)

# use only for tv column
X_train = X_train/10
X_test = X_test/10

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# iii. Also evaluate the model using scores RMSE

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"Root Mean Squared Error (RMSE): {rmse}")


# 1-3
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.title('Actual vs Predicted Sales')
plt.xlabel('Radio')
plt.ylabel('Sales')
plt.legend()
plt.show()

# 4-6
plt.figure(figsize=(12,6))

indices = np.arange(len(y_test))
plt.bar(indices - 0.2, y_test, width=0.4, label='Actual Sales', color='blue')
plt.bar(indices + 0.2, y_pred, width=0.4, label='Predicted Sales', color='red')

plt.title('Comparison of Actual vs Predicted Sales')
plt.xlabel('Data Points')
plt.ylabel('Sales')
plt.legend()

plt.show()