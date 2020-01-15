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



for iltest in range(len(test)):
    distance=[]
    distanceid=[]
    for item in range(len(data)):
       datalist= data.iloc[item]
       testlist=test.iloc[iltest]
       number1=float(testlist[0])-float(datalist[0]);
       number2=float(testlist[1])-float(datalist[1]);
       number3=float(testlist[2])-float(datalist[2]);
       number4=float(testlist[3])-float(datalist[3]);
       sumknn1=pow(number1,2)
       sumknn2=pow(number2,2)
       sumknn3=pow(number3,2)
       sumknn4=pow(number4,2)
       sqrknn=np.sqrt(sumknn1+sumknn2+sumknn3+sumknn4)
       distance.append(sqrknn)
       distanceid.append(item)
       

    for passnum in range(len(distance)-1,0,-1):
        for i in range(passnum):
            if distance[i]>distance[i+1]:
                tempid=distanceid[i]
                temp = distance[i]
                distanceid[i]=distanceid[i+1]
                distance[i] = distance[i+1]
                distanceid[i+1]=tempid
                distance[i+1] = temp


    neighbors=[]
    for item in range(3):
        neighbors.append(data.iloc[distanceid[item]])
    neighbo = pd.DataFrame(neighbors)
    print(neighbo)
        
   










