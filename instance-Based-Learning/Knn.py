import numpy as np
import csv
import pandas as pd
from matplotlib import pyplot as plt
import math
from sklearn.model_selection import train_test_split


df = pd.read_csv("maleFemale.csv")

x1 = np.array(df["Height"].head(70)) # height
x2 = np.array(df["Weight"].head(70)) # weithgt 
y  = np.array(df["Gender"].head(70))

x = []
for i in range(len(x1)):
     x.append([x1[i],x2[i]])
    
x_train,x_test,y_trian,y_test = train_test_split(x,y,test_size=0.3)  


plt.subplot(1,1,1)

for i in range(len(x1)):
                if(y[i]=="Male"):
                  plt.scatter(x1[i],x2[i],color="red",label="Male")
                
                else:
                  plt.scatter(x1[i],x2[i],color="blue",label="Female")
               

            
            
plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Male-female data")
#plt.legend(loc='upper right')
plt.show()
distance = []
def eucliDistance(x_test):
    
    for i in range(len(x)):
        for j in range(len(x_train[i])):
         dis = np.sqrt(np.sum(np.square(x_test - x_train[i][j])))
         # add it to list of distances 
         distance.append([dis, i])

 

