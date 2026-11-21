#tasks
#انشاء مصفوفة احادية البعد تحتوي على ارقام زوجية من ٢ الى ١٢
import numpy as np
arr1=np.arange(2,13,2)
print(arr1)
#انشاء مصفوفة ثنائية الابعاد وجميع عناصرها تساوي 5
arr2=np.full((3,3),5)
print(arr2)
#طباعة عدد الابعاد واجمالي عدد العناصر للمصفوفة الثانية
print(arr2.ndim)
print(arr2.size)
grades=np.array([75,88,92,60,45,98])
print(np.mean(grades))
print(np.min(grades))
print(np.max(grades))
print(grades[grades>=60])
print(np.sort(grades))



