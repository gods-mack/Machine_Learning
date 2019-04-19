#!/usr/bin/env python
# coding: utf-8

# In[232]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score 
from sklearn.metrics import r2_score


# In[233]:


data = pd.read_csv("housing.csv")


data.head()


# In[234]:



X = (np.c_[data['RM'],data['LSTAT'],data['PTRATIO']])
Y = (np.c_[data['MEDV']])



x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size = 0.2)


# In[235]:


clf = LinearRegression()
clf.fit(x_train,y_train)

y_pred = clf.predict(x_test)


# In[241]:


#print ("Accuracy : ", 
#accuracy_score(y_test,y_pred)) 

print(" Prediction Score on Testing data ")
print(r2_score(y_test,y_pred))


# In[ ]:





# In[ ]:





# In[ ]:




