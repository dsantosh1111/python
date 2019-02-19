# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 23:52:46 2019

@author: santosh
"""

from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
data = pd.read_csv("C:/Users/Santhosh/Downloads/iris.csv")
iris=datasets.load_iris()
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.4,random_state=2)

model=svm.SVC(kernel='linear')
model.fit(x_train,y_train)
print(model)
y_pred=model.predict(x_test)

print(y_pred)
print(y_test)
print(metrics.accuracy_score(y_test,y_pred))
print(metrics.precision_score(y_test,y_pred,average='macro'))
print(metrics.f1_score(y_test,y_pred,average='macro'))
print(metrics.recall_score(y_test,y_pred,average='macro'))