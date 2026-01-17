#Student Performance Prediction using linear and logistic regression
#Author:Aditi Sharma
#Problem Statement
'''We want to predict a student’s academic performance based on:
Study hours
Attendance
Past scores
Other factors
This is a supervised machine learning problem:
Input → student data
Output → predicted performance'''
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_squared_error,r2_score
data = pd.read_csv("data/student-data.csv")
print(data.head())
print(data.isnull().sum())
# Linear Regression is used to predict continuous Final_Score, that's why I am using that.
X = data[['Study_Hours','Attendance','Previous_Score']]
Y = data['Final_Score']
print("X (features)")
print(X.head())
print("Y (Final_score)")
print(Y.head())
# Linear Regression trained using MSE minimization (MLE under Guassian noise)
data['Pass_Fail'] = data['Final_Score'].apply(lambda x:1 if x >= 60 else 0)
y_class = data['Pass_Fail']
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2, random_state = 42)
lin_reg = LinearRegression()
lin_reg.fit(X_train,Y_train)
print("Intercept",lin_reg.intercept_)
print("Cofficients:",lin_reg.coef_)
print(np.corrcoef(data['Study_Hours'],data['Final_Score']))
Y_pred = lin_reg.predict(X_test)
mse = mean_squared_error(Y_test,Y_pred)
r2 = r2_score(Y_test,Y_pred)
comparison = pd.DataFrame({"Actual":Y_test, "Predict":Y_pred})
print(comparison)