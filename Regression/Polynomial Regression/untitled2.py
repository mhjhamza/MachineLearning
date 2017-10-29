# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
#from sklearn.cross_validation import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""


from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 3)
poly_x = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(poly_x, y)

#res = lin_reg_2.predict(poly_reg.fit_transform(np.array([[5]])))


plt.scatter(X,y, color = 'red')
plt.plot(X, lin_reg.predict(X))
plt.xlabel('Years')
plt.ylabel('Salary')
plt.show()



plt.scatter(X,y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)))
plt.xlabel('Years')
plt.ylabel('Salary')
plt.show()