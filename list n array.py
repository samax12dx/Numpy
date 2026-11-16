import numpy as np
x = np.array([1,2,3])
print(x)
print(x*2)
y= [1,2,3]
print(y)
print(y*2)
#1D array
a = np.array([10,20,30,40])
print("1D array = " , a)
print("\n")
#2D array
b = np.array([[10,20,30,40],[50,60,70,80]])
print("2D array =  " , b)
print("\n")
#3D array
c = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("3D array = " , c)
print ( "\n")
#معرفة ابعاد المصفوفة باستخدام ndim
d = np.array([1,2,3])
print(d.ndim)
e=np.array([[1,2,3],[4,5,6]])
print(e.ndim)
