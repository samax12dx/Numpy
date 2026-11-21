import numpy as np
#مصفوفة ممتلئة بقيمة محددة
full_arr=np.full((2,2),7)
print(full_arr)
print("\n")
#مصفوفة بارقام عشوائة عشرية
rand_floats=np.random.rand(2,2)
print(rand_floats)
print("\n")
#مصفوفة بارقام عشوائة صحيحة
rand_ints =np.random.randint(1,10,(2,2))
print(rand_ints)
# انشاء نطاق ارقام متسلسل
print("\n")
s = np.arange(0,10,2)
print(s)
m=np.arange(0,10,3)
print(m)
print("\n")
arr = np.array([[10,20,30],[40,50,60]])
#معرفة عدد ابعاد المصفوفة
print(arr.ndim)
#حساب العدد الاجمالي للعناصر الموجودة في المصفوفة
print(arr.size)
#الوصول الى عنصر معين داخل المصفوفة
print(arr[1,2])
#تقطيع
print (arr[:,1])
print(arr[:,0])
print(arr[1,2])
print(arr[0,:])
print(arr[1,:])
