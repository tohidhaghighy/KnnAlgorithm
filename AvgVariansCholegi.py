import pandas as pd
import numpy as np
import math
import operator
import statistics
import matplotlib.pyplot as plt

# تعریف کردن نام ستون ها
col=['sepal_length','sepal_width','petal_length','petal_width','class']
# خواندن داده ها از فایل و ریختن ان داخل data  
data = pd.read_csv('iris.csv',names=col)

# توضیحاتی در مورد فایل موجود
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

# تعریف 4 ارایه هر ویژگی یک ارایه مخصوص خود را دارد
avgarray1=[]
avgarray2=[]
avgarray3=[]
avgarray4=[]

# پر کردن مقادیر ارایه ها برای انجام محاسبات اماری روی ان ها
for item in range(len(data)):
   datalist= data.iloc[item]
   avgarray1.append(datalist[0])
   avgarray2.append(datalist[1])
   avgarray3.append(datalist[2])
   avgarray4.append(datalist[3])

# چاپ و نمایش ان به کاربر 
print(avgarray1)
print(avgarray2)
print(avgarray3)
print(avgarray4)

# گرفتن میانگین هر کدام از ارایه ها با جمع انها و تقسیم انها بر تعدادشان
avg1=sum(map(float,avgarray1))/150
avg2=sum(map(float,avgarray2))/150
avg3=sum(map(float,avgarray3))/150
avg4=sum(map(float,avgarray4))/150

# چاپ مقادیر میانگین ها
print(" Avarage 1 : ")
print(avg1)
print(" Avarage 2 : ")
print(avg2)
print(" Avarage 3 : ")
print(avg3)
print(" Avarage 4 : ")
print(avg4)

#یافتن واریانس مقدار هر متغیر - مینگین ان به قوه 2 تقسیم بر تعداد
varians1=statistics.pvariance(avgarray1)
varians2=statistics.pvariance(avgarray2)
varians3=statistics.pvariance(avgarray3)
varians4=statistics.pvariance(avgarray4)
print(" Variance 1 : ")
print(varians1)
print(" Variance 2 : ")
print(varians2)
print(" Variance 3 : ")
print(varians3)
print(" Variance 4 : ")
print(varians4)

# یافتن انحراف از معیار هر کدام از ویژگی ها
print(" Standard deviation 1 : ")
print(np.sqrt(varians1))
print(" Standard deviation 2 : ")
print(np.sqrt(varians2))
print(" Standard deviation 3 : ")
print(np.sqrt(varians3))
print(" Standard deviation 4 : ")
print(np.sqrt(varians4))

# مرتب سازی ارایه ها برای یافتن میانه انها
avgarray1.sort()
avgarray2.sort()
avgarray3.sort()
avgarray4.sort()

# یافتن و چاپ میانه اعداد هر دسته
print(" Middle 1 : ")
print(avgarray1[75])
print(" Middle 2 : ")
print(avgarray2[75])
print(" Middle 3 : ")
print(avgarray3[75])
print(" Middle 4 : ")
print(avgarray4[75])


# رسم نمودار های توزیع و فهمیدن توزیع مقادیر هر ارایه
plt.hist(avgarray1,bins=100,normed=False)
plt.xlabel('Rang of Data')
plt.ylabel('petal_width')
plt.title(' petal_width of Distribution 1')
plt.show()


plt.hist(avgarray2,bins=100,normed=False)
plt.xlabel('Rang of Data')
plt.ylabel('petal_width')
plt.title(' petal_width of Distribution 2')
plt.show()


plt.hist(avgarray3,bins=100,normed=False)
plt.xlabel('Rang of Data')
plt.ylabel('petal_width')
plt.title(' petal_width of Distribution 3')
plt.show()


plt.hist(avgarray4,bins=100,normed=False)
plt.xlabel('Rang of Data')
plt.ylabel('petal_width')
plt.title(' petal_width of Distribution 4')
plt.show()

