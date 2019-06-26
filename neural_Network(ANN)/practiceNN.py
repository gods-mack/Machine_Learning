import numpy as np 
import random
import math

def sigmoid(x):
	return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x):
	return x * (1-x)	


X = np.array([[0,0,1],
			  [1,1,1],
			  [1,0,1],
			  [0,1,1]])

y = np.array([[0,1,1,0]]).T

np.random.seed(1)
weights = 2*np.random.random((3,1))-1

print("before weights ")
print(weights)

for iteration in range(1000):

	input_layer = X
	
	a = sigmoid(np.dot(input_layer,weights))	

	error = (y - a)
     
	ajust = 2*error * sigmoid_dervative(y_pred)
	weights += np.dot(input_layer.T,ajust)


print("original Output ")    
print(y)
print(" prdicted output(y^)")
print(a)
print("cost ")
print(error)




