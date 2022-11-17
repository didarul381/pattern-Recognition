# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 12:24:01 2022

@author: User
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from  sklearn.linear_model import LinearRegression
data=pd.read_csv("Mydata.csv")
print(data)

plt.scatter(data["Area"],data["Price"])
data.isnull().any()
plt.xlabel("size")
plt.ylabel("Area")
plt.title("price perdiction")
x=data[["Area"]]
y=data["Price"]
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.30,random_state=(1))
xtrain
ytrain

reg=LinearRegression()
reg.fit(xtrain,ytrain)

reg.predict([[3000]])







