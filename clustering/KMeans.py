
#!/usr/bin/env python
# coding: utf-8

# In[34]:


from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler


# In[68]:


df = pd.read_csv("income.csv")
plt.scatter(df['Age'],df['Income($)'])


# In[72]:


clf = KMeans(n_clusters=3)

scaler = MinMaxScaler()
scaler.fit(df[['Income($)']])


df['Income($)']  = scaler.transform(df[['Income($)']])

scaler.fit(df[['Age']])
df['Age'] = scaler.transform(df[['Age']])

df


# In[87]:


y_predict = clf.fit_predict(df[['Age','Income($)']])

df['cluster'] = y_predict

df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]

plt.figure()

plt.scatter(df1.Age,df1['Income($)'],color="green")
plt.scatter(df2.Age,df2['Income($)'],color="blue")
plt.scatter(df3.Age,df3['Income($)'],color="red")

plt.xlabel("Age")
plt.ylabel("Income($)")
plt.legend()


# In[90]:


# Lets Amrk the cluster Center

clf.cluster_centers_

plt.scatter(df1.Age,df1['Income($)'],color="green")
plt.scatter(df2.Age,df2['Income($)'],color="blue")
plt.scatter(df3.Age,df3['Income($)'],color="red")
plt.scatter(clf.cluster_centers_[:,0],clf.cluster_centers_[:,1],color="black",marker='*')

plt.xlabel("Age")
plt.ylabel("Income($)")
plt.legend()


# In[101]:


# Elbow technique
'''in the real world we have around more than 10 feature parameter so it is 
very difficult to plot on scatter plot ,here we use "Elbow technique" to get efficent value of K '''

k_range = range(1,10)
sse = []  # sequred sum error

for k in k_range:
    clf = KMeans(n_clusters=k)
    clf.fit(df[['Age','Income($)']])
    sse.append(clf.inertia_)
    

plt.plot(k_range,sse)
plt.xlabel("K-value")
plt.ylabel("sum sequred error(SSE)")

# our efficient K-value is present at Elbow Postion of graph , Here(i.e 3)


# In[ ]:




