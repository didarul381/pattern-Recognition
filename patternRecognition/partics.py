# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:05:41 2022

@author: Didarul Alam
"""
#1.import modules or libary
import pandas as pd
import numpy as np

#2.Load dataset
dataset = pd.read_csv("Social_Network_Ads.csv")
#print(dataset)
#3.separet independent and dependent variable
x=dataset.iloc[:,2:4]
y=dataset.iloc[:,-1]
#print(x,y)

#4.Handle missing data
#print(dataset.isnull().sum)

#5.Drop missing values or records
#dataset.dropna(inplace=True)

#6.Replace missing value
from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy = 'mean')
imputer.fit(x)
x = imputer.transform(x)
print(x)


