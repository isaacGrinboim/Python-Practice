import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# Load Bitcoin price data
data = pd.read_csv('prices.csv')
points = [(i + 1, float(price)) for i, price in enumerate(data['price'][::-1])]

X = np.array([point[0] for point in points]).reshape(-1, 1)
y = np.array([point[1] for point in points])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit Polynomial Regression model (Degree = 7)
degree = 7
poly_features = PolynomialFeatures(degree=degree)
X_train_poly = poly_features.fit_transform(X_train)
X_test_poly = poly_features.transform(X_test)
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Predictions on training and testing data
y_train_pred = model.predict(X_train_poly)
y_test_pred = model.predict(X_test_poly)

# Create a figure and axis for the plot
plt.figure(figsize=(10, 6))

# Plot the training data in blue
plt.scatter(X_train, y_train, color='blue', label='Training Data')

# Plot the testing data in red
plt.scatter(X_test, y_test, color='red', label='Testing Data')

# Plot the polynomial regression curve in green
X_range = np.arange(X.min(), X.max() + 1, 0.1).reshape(-1, 1)  # Extend the X_range
X_range_poly = poly_features.transform(X_range)
y_range_pred = model.predict(X_range_poly)
plt.plot(X_range, y_range_pred, color='green', label=f'Polynomial (Degree {degree})')

plt.xlabel('Time')
plt.ylabel('Bitcoin Price')
plt.title('Bitcoin Price Prediction (Polynomial Regression)')
plt.legend()
plt.show()


coefficients = model.coef_

# The coefficients correspond to the polynomial terms, starting from the highest-degree term
print("Coefficients:", coefficients)