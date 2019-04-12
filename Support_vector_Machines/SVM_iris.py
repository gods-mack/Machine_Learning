
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn import svm

iris = load_iris()

x = iris.data[:, :2] 
y = iris.target

''' our svm classifier clf object here we can change kernel type like linear,rbf,sigmoid
C = Penalty parameter C of the error term. It also controls the trade off between smooth decision boundary 
and classifying the training points correctly. C=1,10,100

gamma: Kernel coefficient for ‘rbf’, ‘poly’ and ‘sigmoid’. Higher the value of gamma, 
will try to exact fit the as per training data set 
i.e. generalization error and cause over-fitting problem.

'''
clf = svm.SVC(kernel='linear',C=1,gamma='scale').fit(x,y)

x_min, x_max = x[:, 0].min() - 1, x[:, 0].max() + 1
y_min, y_max = x[:, 1].min() - 1, x[:, 1].max() + 1
h = (x_max/x_min)/100

xx, yy = np.meshgrid(np.arange(x_min, x_max, h),  # mashgrid array
 np.arange(y_min, y_max, h))

plt.subplot(1,1,1)
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]) # ravel() = it does flatten i.e arrange all elemnt in single row
Z = Z.reshape(xx.shape)
#print(Z)
plt.contourf(xx,yy,Z, cmap=plt.cm.Paired, alpha=0.5)
plt.scatter(x[:, 0], x[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.xlim(xx.min(), xx.max())
plt.title('SVC with linear kernel')
plt.show()
