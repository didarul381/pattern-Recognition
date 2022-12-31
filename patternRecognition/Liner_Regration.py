# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:49:06 2022

@author: User
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data=pd.read_csv("Mydata.csv");
print(data)

plt.scatter(data["Area"],data["Price"])
plt.xlabel("size")
plt.ylabel("Area")
x=data["Area"]
y=data[["Price"]]
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.30,random_state=1)

reg=LinearRegression()
reg.fit(xtrain,ytrain)
reg.predict([3500])

print(reg.predict([3500]))

