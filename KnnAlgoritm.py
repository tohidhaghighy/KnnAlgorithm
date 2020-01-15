import pandas as pd
import numpy as np
import math
import operator
import statistics
import random
import matplotlib.pyplot as plt

col=['sepal_length','sepal_width','petal_length','petal_width','class']
data = pd.read_csv('iris.csv',names=col)


#a=input("enter first number : ")
#b=input("enter second number : ")
#c=input("enter third number : ")
#d=input("enter fored number : ")

#testSet = [[a, b, c, d]]



randnum=random.randint(0,150)
testSet = []

testSet.append(data.iloc[randnum])
test = pd.DataFrame(testSet)
print(test)
distance=[]
distanceid=[]


#پیدا کردن فاصله اقلیدسی در بین دو نقطه و افزودن به لیست
for item in range(len(data)):
   datalist= data.iloc[item]
   testlist=test.iloc[0]
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


print(distance)
print(distanceid)

#مرتب سازی ارایه فاصله با بابل سورت به ترتیب سعودی
for passnum in range(len(distance)-1,0,-1):
        for i in range(passnum):
            if distance[i]>distance[i+1]:
                tempid=distanceid[i]
                temp = distance[i]
                distanceid[i]=distanceid[i+1]
                distance[i] = distance[i+1]
                distanceid[i+1]=tempid
                distance[i+1] = temp


print(distance)
print(distanceid)

# از 3 تا 15 k  را تغییر میدهیم 
#و همسایه های نزدیک نقطه تصادفی را میابیم
neighbors=[]
fault=[]
numscall=[]
for kitem in range(3,15):
   neighbors=[]
   numscall.append(kitem)
   faultcounter=0
   for item in range(1,kitem+1):
        neighbors.append(data.iloc[distanceid[item]])
        #تشخیص اینکه مربوط به کدام گل هست و پیدا کردن خطاها برای رسم نمودار
        if randnum<50:
               if distanceid[item]>50:
                      faultcounter+=1
        if randnum>50 and randnum<100 :
               if distanceid[item]< 50 and distanceid[item]> 100:
                      faultcounter+=1
        if randnum>100 :
               if distanceid[item]< 100:
                      faultcounter+=1 
   fault.append(faultcounter)
   print(faultcounter)                                            
   print(pd.DataFrame(neighbors))
   print("*********************************************")
          
#رسم نمودار از روی اعداد خطاها
plt.plot(numscall,fault)
plt.xlabel('k ')
plt.ylabel('fault count')
plt.title(' find fault count')
plt.show()


