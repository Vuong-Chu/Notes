# Notes of Python

### 1. main function - Best practice in Python
* Put most code into a function or class.
* Use __name__ to control execution of your code.
* Create a function called main() to contain the code you want to run.
* Call other functions from main().
```python
def main():
  println("Hello, World!")
  
if __name__=="__main__":
  main()

```

### 2. Python for econometrics

```python
import numpy as np
import math
from scipy import linalg, sparse

# Creating matrix
A = np.mat([[6,3],[9,10]])
print(A)
B = np.mat([[15,4],[8,-2],[4,1]])
print(B)
C = np.mat([[-4,-5,4],[-6,0,-13]])
print(C)
D = np.mat([[3,0],[0,3]])
print(D)
E = np.ones(3)
print(E)
F = np.zeros(4)
print(F)
G = np.eye(3,3)
print(G)

# Matrix arithmetic
print(A + D)
print(D - A)
print(A/3)
print(np.round(np.linalg.inv(A),2)) #Round 2 decimals
print(B - C.T)
print(B.dot(A))
print(A.dot(B.T))
print(np.multiply(D,A)) #Element-wise multiplication or the Hadamard product
print((B-C.T).dot(D))
print(np.multiply(C.dot(B),D))
print(B.T.dot(C.T).dot(A.dot(D)))

#Reshaping and replicating matrix
print(np.tile(A,(2,1)))
print(np.tile(A.T,(2,1)))
print(np.reshape(C.T,(2,3)).T) #Matlab reshape(C,3,2)
print(np.tile(D,(2,2)))
print(np.tile(np.reshape(A.T,(1,4)),(1,2)))
print(np.reshape(np.tile(A.T,(1,2)),(1,8)))

#Indexing matrix
#Notes: Python counts from 0
print(A.item(1,1)) #Pick 1 value
print(A[1,1])      #Pick 1 value
print(C[:,1])
print(B[(0,2),:])  #Pick random rows
print(B[0:2,:])    #Warnings 0:2 -> 2 first rows
print(B[1:3,1])

#Modyfying matrix variables
A[1,1]=3
print(A)
B[1,:] = np.mat([[1,1]])
print(B)
print(C[:,1:]) #all except for first column
print(C[:,2])  #last column
print(C[:,:-1]) #all except for last column
print(C[:,-1])  #last column

#Creating variables from existing matrices and function
print(np.concatenate((A,B),axis=0))
print(np.concatenate((C,A),axis=1))
print(np.mat(np.random.normal(0,1,(10,1))))
print(np.mat(np.random.normal(3,10,(10,1))))
print(np.cumsum(B,axis=0))
print(np.diff(B,axis=0))
print(np.diag(A))
full_name = np.mat(["Chu","Nhat","Minh","Vuong"])
print(full_name)
list = [A,full_name,C]
print(list)
H = np.random.normal(0,1,(15,4))
print(H)
print(np.logical_and(H<1, H>0)) #Logical matrix
```
