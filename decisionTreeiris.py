import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 
from sklearn.metrics import confusion_matrix 

iris = load_iris()

def splitData():
    x = iris.data
    y = iris.target
     
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=100)
    return x_train,x_test,y_train,y_test

def trainTest():
    clf =  DecisionTreeClassifier(criterion = "gini", 
			random_state = 100,max_depth=3, min_samples_leaf=5)
    clf.fit(x_train,y_train)
    return clf 

def prediction(x_test,clf_object):
   y_pred = clf_object.predict(x_test)
   print(y_pred)
   return y_pred

def accuracy(y_test, y_pred): 
	
	print("Confusion Matrix: ", 
	confusion_matrix(y_test, y_pred) )
	
	print ("Accuracy : ", 
	accuracy_score(y_test,y_pred)*100) 
	
	print("Report : ", 
	classification_report(y_test, y_pred)) 

     

x_train,x_test,y_train,y_test = splitData()
y_pred = prediction(x_test,trainTest())
accuracy(y_test,y_pred)    



