# -*- coding: utf-8 -*-
"""a4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KnfpcCvhM1UeIqYhB1oOjSiZJUMuQfSB
"""

!pip install ucimlrepo
from ucimlrepo import fetch_ucirepo, list_available_datasets
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import matplotlib.pyplot as plt

white_wine = pd.read_csv('/content/winequality-white.csv', sep=';')

#1
white_wine.describe()

#2
white_wine.corr()

#3
ax = (white_wine['quality']).plot.hist()
plt.title('Frequency of each Wine Quality Level')
ax.set_xlabel('Quality')

#4
sns.violinplot(data=white_wine, x='quality', y='fixed acidity', inner='quart').set_title('Fixed Acidity Levels per Wine Quality')

sns.violinplot(data=white_wine, x='quality', y='volatile acidity', inner='quart').set_title('Volatile Acidity Levels per Wine Quality')

sns.violinplot(data=white_wine, x='quality', y='citric acid', inner='quart').set_title('Citric Acid Concentration per Wine Quality')

sns.violinplot(data=white_wine, x='quality', y='residual sugar', inner='quart').set_title('Residual Sugar Concentration per Wine Quality')

sns.violinplot(data=white_wine, x='quality', y='chlorides', inner='quart').set_title('Chloride Concentration per Wine Quality')

sns.violinplot(data=white_wine, x='quality', y='free sulfur dioxide', inner='quart').set_title('Free Sulfur Dioxide Levels per Wine Quality')

sns.violinplot(data=white_wine, x='quality', y='total sulfur dioxide', inner='quart').set_title('Total Sulfur Dioxide Levels per Wine Quality')

sns.violinplot(data=white_wine, x='quality', y='density', inner='quart').set_title('Density per Wine Quality')

sns.violinplot(data=white_wine, x='quality', y='pH', inner='quart').set_title('pH Levels per Wine Quality')

sns.violinplot(data=white_wine, x='quality', y='sulphates', inner='quart').set_title('Sulphate Concentration per Wine Quality')

sns.violinplot(data=white_wine, x='quality', y='alcohol', inner='quart').set_title('Alcohol Content per Wine Quality')

#5
model = LinearRegression()

model.fit(white_wine[['alcohol']], white_wine['quality'])

print(f'Intercept = {model.intercept_}')
print(f'Coefficient = {model.coef_[0]}')

fitted = model.predict(white_wine[['alcohol']])

RMSE = np.sqrt(mean_squared_error(white_wine['quality'], fitted))
r2 = r2_score(white_wine['quality'], fitted)

print(f'RMSE = {RMSE} and r2 = {r2}')

white_wine.plot.scatter(x='alcohol', y='quality')
plt.title('Relationship Between Alcohol Content and Wine Quality')

#6
X = white_wine[['volatile acidity', 'alcohol', 'density']]
y = white_wine['quality']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

fitted = model.predict(X_test)

MSE = mean_squared_error(y_test, fitted)
RMSE = np.sqrt(MSE)
r2 = r2_score(y_test, fitted)

print(f'Intercept: {model.intercept_}')
print(f'Coefficients: {model.coef_}')

print(f'RMSE = {RMSE} and r2 = {r2}')