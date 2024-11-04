import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from LinearRegression import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("dataset/car/car data.csv")

print(df.head())
print(df.info())

# Convert 'transmission' column to binary values: 0 for 'Manual', 1 for 'Automatic'
df["Transmission"] = df["Transmission"].map({"Manual": 0, "Automatic": 1})
df["Fuel_Type"] = df["Fuel_Type"].map({"Petrol": 0, "Diesel": 1})
df["Seller_Type"] = df["Seller_Type"].map({"Dealer": 0, "Individual": 1})
df["Year"] = df["Year"] / 100
df["Kms_Driven"] = df["Kms_Driven"] / 1000
df = df.dropna()

sns.scatterplot(x="Kms_Driven", y="Selling_Price", data=df)
plt.title("Kms_Driven vs Selling_Price")
plt.show()

# 7. Selling prices w.r.t year bought
X1 = df[["Year"]]  # Input
y1 = df["Selling_Price"]  # Output

# 8. Selling prices w.r.t km driven
X2 = df[["Kms_Driven"]]  # Input
y2 = df["Selling_Price"]  # Output

# 9. Selling prices w.r.t transmission
X3 = df[["Transmission"]]  # Input
y3 = df["Selling_Price"]  # Output

# 10. Selling prices w.r.t owner
X4 = df[["Owner"]]  # Input
y4 = df["Selling_Price"]  # Output

# 11. Selling prices w.r.t year bought and km driven
X5 = df[["Year", "Kms_Driven"]]  # Input
y5 = df["Selling_Price"]  # Output

# 12. Selling prices w.r.t year bought and transmission
X6 = df[["Year", "Transmission"]]  # Input
y6 = df["Selling_Price"]  # Output

# 13-14. Selling prices w.r.t year bought and owner
X7 = df[["Year", "Owner"]]  # Input
y7 = df["Selling_Price"]  # Output

# 15. Selling prices w.r.t km driven and transmission
X8 = df[["Kms_Driven", "Transmission"]]  # Input
y8 = df["Selling_Price"]  # Output

# 16. Selling prices w.r.t km driven and owner
X9 = df[["Kms_Driven", "Owner"]]  # Input
y9 = df["Selling_Price"]  # Output

# 17-18. Selling prices w.r.t transmission and owner
X10 = df[["Transmission", "Owner"]]  # Input
y10 = df["Selling_Price"]  # Output

X11 = df.drop(["Selling_Price", "Car_Name"], axis=1)
y11 = df["Selling_Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X1, y1, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_pred = np.clip(y_pred, a_min=0, a_max=None)

# rmse = np.sqrt(np.mean((y_test - y_pred) ** 2))
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"Root Mean Squared Error (RMSE): {rmse}")

# 7-10
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.title('Year vs Selling_Price')
plt.xlabel('Year')
plt.ylabel('Selling_Price')
plt.legend()
plt.show()

 # 11-18
plt.figure(figsize=(12,6))
indices = np.arange(len(y_test))
plt.bar(indices - 0.2, y_test, width=0.4, label='Actual Price', color='blue')
plt.bar(indices + 0.2, y_pred, width=0.4, label='Selling Price', color='red')
plt.title('Comparison of Actual vs Predicted Price')
plt.xlabel('Data Points')
plt.ylabel('Selling Price')
plt.legend()
plt.show()