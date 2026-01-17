import pandas as pd 
import numpy as np
import pickle
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
data = pd.read_csv("data/student-data.csv")
data['Pass_Fail'] = data['Final_Score'].apply(lambda x:1 if x >= 60 else 0)
X =data[["Study_Hours","Attendance","Previous_Score"]]
Y = data["Pass_Fail"]
X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=0.2,random_state=42)
log_reg = LogisticRegression()
log_reg.fit(X_train,Y_train)
Y_pred = log_reg.predict(X_test)
print("Accuracy",accuracy_score(Y_test,Y_pred))
print("Confusion Matrix:\n",confusion_matrix(Y_test,Y_pred))
print("Classification_Report:\n",classification_report(Y_test,Y_pred))

y_prob = log_reg.predict_proba(X_test)
print(y_prob[:5])
y_pass_prob = y_prob[:,1]
y_custom_pred = np.where(y_pass_prob >= 0.6,1,0)
print("Accuracy with 0.6 threshold:",accuracy_score(Y_test,y_custom_pred))

with open("model.pkl","wb") as f:
    pickle.dump(log_reg,f)