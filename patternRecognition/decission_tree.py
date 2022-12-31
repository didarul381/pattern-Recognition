# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 15:30:16 2022

@author: User
"""

import pandas as pd
dataset=pd.read_csv('Social_Network_Ads.csv');
x=dataset.iloc[:,[2,3]].values;
y=dataset.iloc[:,4].values;

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.tree import DecisionTreeClassifier
classifer=DecisionTreeClassifier(criterion='entropy',random_state=(0));
classifer.fit(x_train,y_train);

y_pred=classifer.predict(x_test)

#print(y_pred)

from sklearn.metrics import confusion_matrix
cm= confusion_matrix(y_test,y_pred)
print(cm)