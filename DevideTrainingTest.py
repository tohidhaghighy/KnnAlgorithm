import pandas as pd
import numpy as np
import math
import operator
import statistics
import random
col=['sepal_length','sepal_width','petal_length','petal_width','class']
data = pd.read_csv('iris.csv',names=col)

print("first five rows")
print(data.head())
print("*******")
print("colums",data.columns)
print("*******")
print("shape",data.shape)
print("*******")
print("size",data.size)

print(data['sepal_width'].value_counts())
print("*******")
print(data.describe())

#تعریف لیست های تست و اموزش و ایدی انها
NumberTestList=[]
TrainingList=[]
TestList=[]

# انتخاب 30 تا خط از لیست ورودی به صورت رندوم برای لیست تست
for item in range(30):
   randnum=random.randint(0,150)
   NumberTestList.append(randnum)
   datalist= data.iloc[randnum]
   TestList.append(datalist)

# تبدیل ان به جدول برای نمایش بهتر
test = pd.DataFrame(TestList)
print("Test list of dataset 20% : ")
print(test)

print("Number Of Test List in dataset 20% Test : ")
print(NumberTestList)

# نمایش 120 تا خط از داده ها در لیست اموزش
for item in range(150):
    if item not in NumberTestList:
        datalist= data.iloc[item]
        TrainingList.append(datalist)

# تبدیل ان به جدول برای نمایش بهتر 
test = pd.DataFrame(TrainingList)
print("Training list of dataset 80% : ")
print(test)
