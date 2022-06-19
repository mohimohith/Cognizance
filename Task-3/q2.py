import numpy as np
lst1=input("enter the 1 st array : ").split()
x = np.array(lst1)
x=[int(i) for i in x]
lst2=input("enter the 2nd array  : ").split()
y = np.array(lst2)
y=[int(i) for i in y]
print("First array:")
print(x)
print("Second array:")
print(y)
print("Test above two arrays are equal or not!")
array_equal = True
if len(x) == len(y):
    for i in range(0,len(x)):
        if x[i]!=y[i]:
            array_equal =False
        else:
            pass
else:
    array_equal =False
print(array_equal)