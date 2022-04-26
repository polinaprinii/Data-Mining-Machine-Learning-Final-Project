"""
This file continues step four of the KDD methodology - Data Mining.
Here we look to apply K-Nearest-Neighbour Regression analysis to our dataset.
"""

# Importing needed libraries:
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import math
from sklearn import metrics
import matplotlib.pyplot as plt


# Importing data:
df = pd.read_csv('/Users/polinaprinii/Desktop/Project Datasets/Flight Delays for 2019 for the USA/Selection_pre_PCA.csv')
print(df.head(5))

# Next we move to separating our features from our target.
X = df.drop('departure_delay', axis=1)
y = df['departure_delay']

# Splitting the data into a train and test group using a 30%/70% split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

# Standardising data:
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Applying K-Nearest Neighbour Regression Analysis:
regr = KNeighborsRegressor(11)
regr.fit(X_train, y_train)
y_pred = regr.predict(X_test)

# Interpreting the results:
print(round(regr.score(X_test, y_test), 2), '\n')
print(mean_squared_error(y_test, y_pred))
rmse = math.sqrt(mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error:", rmse)
#Measuring accuracy on Testing Data
print('Accuracy',100- (np.mean(np.abs((y_test - y_pred) / y_test)) * 100))

# TODO: Determine resolve 'ValueError: operands could not be broadcast together with shapes' when identifying optimum K value.

# import math
# n = len(y)
# index = []
# error = []
# for i in range(1, 10):
#     knn = KNeighborsRegressor(n_neighbors = i)
#     knn.fit(X, y)
#     y_pred = knn.predict(X)
#     rss = sum((y_pred - y)**2)
#     rse = math.sqrt(rss/(n-2))
#     index.append(i)
#     error.append(rse)
# print(index, error)

# test_error = []
# iterations = list(range(1, 31))
# for k in range(1, 31):
#     knn = KNeighborsRegressor(n_neighbors=k)
#     knn.fit(X_train, y_train)
#     y_pred = knn.predict(X_test)
#     error = 1 - knn.score(y_test, y_pred)
#
#     test_error.append(error)
#     print(k, error)
#
#
# plt.figure(figsize=(8, 4), dpi=150)
# plt.plot(range(1, 31), test_error)
# plt.show()

