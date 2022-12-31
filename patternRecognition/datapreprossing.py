
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 20:46:15 2022

 @author: Didarul Alam
"""
############ Data Preprocessing ###############
#Import modules or libraries
import pandas as pd
import numpy as np

#Load dataset
dataset = pd.read_csv("Social_Network_Ads.csv")
'''
#Seperate dependant and independant variables
x = dataset.iloc[:, 2:4].values
y = dataset.iloc[:, -1].values
'''
#Handle missing data
#print(dataset.isnull().sum())
#Drop missing value records or rows
#dataset.dropna(inplace = True)
#dataset.dropna()

'''
#Replace missing values
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy = 'mean')
imputer.fit(x[:, :])
x[:, :] = imputer.transform(x[:, :])

imputer.fit(x)
x = imputer.transform(x)
'''
#Data Encoding: handle categorical data
#One hot encoding
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
x = dataset.iloc[:, 1:3].values
ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],remainder='passthrough')
x = np.array(ct.fit_transform(x))
print(x)

#label or class encoding
#when class contains categorical data like yes or no
from sklearn.preprocessing import LabelEncoder
y = dataset.iloc[:, -1].values
le = LabelEncoder()
y=le.fit_transform(y)
#print(y)
#DataPreprocess.py
#Displaying PercentileCalculation.py.
