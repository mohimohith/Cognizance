import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr)
print("Before Redimensioning dimension is: ",arr.ndim)
arr2=arr.reshape(3,3)
print(arr2)
print("After Redimensioning dimension is  : ",arr2.ndim)