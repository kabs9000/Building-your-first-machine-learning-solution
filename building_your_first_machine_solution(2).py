# -*- coding: utf-8 -*-
"""Building your first machine solution.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cUiJkWgvETjPGHKpkZ81D8kFqkEGpx0X

#Module 2
"""

print("Building your first machine solution")

"""#Module 3"""

import pandas

filename='forestfires.csv'
names = ['X', 'Y', 'month,','day', 'FFMC', 'DMC', 
                'DC', 'ISI', 'temp', 'RH', 'wind', 'rain', 'area']

df= pandas.read_csv(filename, names=names)
print(pandas.isnull(df).sum())

"""#Module 4"""

import numpy
import pandas

pandas.set_option('display.max_rows', 500)
pandas.set_option('display.max_columns', 500)
pandas.set_option('display.width', 1000)

"""## Descriptive Statistics"""

filename='forestfires.csv'
names = ['X', 'Y', 'month','day', 'FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain', 'area']
df= pandas.read_csv(filename, names=names)

print(df.shape)

print(df.dtypes)

print(df.head())

print(df.describe())

print(df.corr(method='pearson'))

print(df.head())

df.month.replace(('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'), (1,2,3,4,5,6,7,8,9,10,11,12))
df.day.replace(('mon','tue','web','thu','fri','sat','sun'), (1,2,3,4,5,6,7), inplace=True)

print(df.head())

"""##Visualizing our data

###Histograms
"""

from matplotlib import pyplot as plt

df.hist(sharex=False, sharey=False, xlabelsize=15, ylabelsize=15, color='brown', figsize=(15,15))
plt.suptitle("Histograms", y=1.00, fontweight='bold', fontsize=40)
plt.show()

"""###Probability Density Function"""

df.plot(kind='density', subplots=True, layout=(7,2), sharex=False, fontsize=16, figsize=(15,15))
plt.suptitle("PDF", y=1.00, fontweight='bold', fontsize=40)
plt.show()

"""###Box and Whisker"""

df.plot(kind='box', subplots=False, layout=(4,4), sharex=False, sharey=False, fontsize=16, figsize=(10,10))
plt.suptitle("Box and Whisker", y=1.00, fontweight='bold', fontsize=40)
plt.show()

"""###Scatter Matrix"""

from pandas.plotting._matplotlib import scatter_matrix
Axes=scatter_matrix(df,figsize=(15,15))
plt.suptitle("Scatter Matrix", y=1.00, fontweight='bold', fontsize=30)
plt.rcParams['axes.labelsize'] = 15
[plt.setp(item.yaxis.get_majorticklabels(), 'size', 15) for item in Axes.ravel()]
[plt.setp(item.xaxis.get_majorticklabels(), 'size', 15) for item in Axes.ravel()]
plt.show

"""###Heatmap Matrix"""

import seaborn as sns
plt.figure(figsize =(11,11))
plt.style.use('default')
sns.heatmap(df.corr(), annot = True)

"""#Module 5"""

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
import numpy as np

"""##Train Test"""

X, y = np.arange(10).reshape((5,2)), range(5)

X

list(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("X_train")
print(X_train)
print("X_test")
print(X_test)
print("y_train")
print(y_train)
print("y_test")
print(y_train)

"""##KFold"""

dataset=range(16) #array from 0 to 15

KFCrossValidator = KFold(n_splits= 4, shuffle=False)
KFdataset = KFCrossValidator.split(dataset)

from sklearn.utils import shuffle
print('{} {:^61} {}'.format('Round', 'Training set', 'Testing set'))
for iteration, data in enumerate(KFdataset, start=1):
  print('{:^9} {} {:^25}'.format(iteration, data[0], str(data[1])))

"""#Module 6

## Training the Model
"""

import warnings
import pandas
from sklearn.linear_model import LinearRegression, ElasticNet, Lasso, Ridge
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split, KFold, cross_val_score

filename= 'forestfires.csv'
names = ['X', 'Y', 'month', 'day', 'FFMC', 'DMC', 'DC', 'ISI', 'temp', 'RH', 'wind', 'rain', 'area']
df= pandas.read_csv(filename,names=names)
df.month.replace(('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'), (1,2,3,4,5,6,7,8,9,10,11,12), inplace=True)
df.day.replace(('mon','tue','wed','thu','fri','sat','sun'), (1,2,3,4,5,6,7), inplace=True)

array = df.values
X = array[:,0:12]
Y = array[:,12]

max_error_scoring = 'max_error'
neg_mean_absolute_error_scoring = 'neg_mean_absolute_error'
r2_scoring = 'r2'
neg_mean_squared_error_scoring = 'neg_mean_squared_error'

models = []
models.append(('LR', LinearRegression()))
models.append(('LASSO', Lasso()))
models.append(('EN', ElasticNet()))
models.append(('Ridge', Ridge())) 
models.append(('KNN', KNeighborsRegressor()))
models.append(('CART', DecisionTreeRegressor()))
models.append(('SVR', SVR()))

# Evaluate models and print results
results = []
names = []
for name, model in models:
    kfold = KFold(n_splits=10, shuffle=True, random_state=7)
    cv_results = cross_val_score(model, X, Y, cv=kfold, scoring=max_error_scoring)
    cv_results2 = cross_val_score(model, X, Y, cv=kfold, scoring=neg_mean_absolute_error_scoring)
    cv_results3 = cross_val_score(model, X, Y, cv=kfold, scoring=r2_scoring)
    cv_results4 = cross_val_score(model, X, Y, cv=kfold, scoring=neg_mean_squared_error_scoring)
    msg = "%s: max error: %f , mean absolute error: %f, r2: %f, mean squared error: %f" % (name, cv_results.mean(), -cv_results2.mean(),cv_results3.mean(),-cv_results4.mean())
    print(msg)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=1, shuffle=True)

lasso_model = Lasso()
lasso_model.fit(X_train, Y_train)

predictions = lasso_model.predict(X_test)
print(predictions)

"""## Deploying the Model"""

import pickle
pickle.dump(lasso_model, open('model.pkl' , 'wb'))
model = pickle.load(open('model.pkl','rb'))

!pip install flask-ngrok
!pip install pyngrok
!ngrok authtoken 2KkojzacpWdqpAJXBc4prDPwvuu_4s9NzgDduFNNaE9Lc6pFZ

from flask import Flask, request
from flask_ngrok import run_with_ngrok
import requests
import numpy as np
from pyngrok import ngrok
app = Flask(__name__)
run_with_ngrok(app) #starts ngrok when app is run

@app.route('/predict',methods = ['POST'])
def homer():
  X = int(request.args.get('X', ''))
  Y = int(request.args.get('Y', ''))
  month = int(request.args.get('month', ''))
  day = int(request.args.get('day', ''))
  FFMC = float(request.args.get('FFMC', ''))
  DMC = float(request.args.get('DMC', ''))
  DC = float(request.args.get('DC', ''))
  ISI = float(request.args.get('ISI', ''))
  temp = float(request.args.get('temp', ''))
  RH = float(request.args.get('RH', ''))
  wind = float(request.args.get('wind', ''))
  rain = float(request.args.get('rain', ''))
  prediction = lasso_model.predict([[X, Y, month,day,FFMC,DMC,DC,ISI,temp,RH,wind,rain]])
  print('***************')
  print(prediction)
  return 'Prediction is ' +str(prediction[0])

  
app.run()