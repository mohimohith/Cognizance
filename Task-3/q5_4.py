import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("before : ",arr.dtype)
arr=arr.astype('float64')
print("After : ",arr.dtype)