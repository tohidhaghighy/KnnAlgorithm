import pandas as pd
import numpy as np
import math
import operator
import statistics
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# تعریف کردن نام ستون ها
col=['sepal_length','sepal_width','petal_length','petal_width','target']
# خواندن داده ها از فایل و ریختن ان داخل data  
data = pd.read_csv('iris.csv',names=col)

data1_flower=[]
for item in range(50):
     datalist= data.iloc[item]
     data1_flower.append(datalist)

data2_flower=[]
for item in range(51,100):
     datalist= data.iloc[item]
     data2_flower.append(datalist)
    
data3_flower=[]
for item in range(101,150):
     datalist= data.iloc[item]
     data3_flower.append(datalist)

print(data1_flower)
print(data2_flower)
print(data3_flower)

#array1
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
x = data.loc[:, features].values
y = data.loc[:,['target']].values
x = StandardScaler().fit_transform(x)

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])

finalDf = pd.concat([principalDf, data[['target']]], axis = 1)

print(finalDf)

array1=[]
array2=[]
array11=[]
array22=[]
array111=[]
array222=[]

for item in range(0,50):
     datalist= finalDf.iloc[item]
     array1.append(datalist[0])
     array2.append(datalist[1])

for item in range(51,100):
     datalist= finalDf.iloc[item]
     array11.append(datalist[0])
     array22.append(datalist[1])

for item in range(101,150):
     datalist= finalDf.iloc[item]
     array111.append(datalist[0])
     array222.append(datalist[1])


plt.scatter(array1,array2,c='red')
plt.scatter(array11,array22,c='green')
plt.scatter(array111,array222,c='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.title(' pca graph')
plt.show()