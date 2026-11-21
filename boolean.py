import numpy as np
#المنطق
arr=np.array([10,20,30,40,15])
filtered =arr[arr>25]
print("values > 25 : " , filtered)
filtered=arr[arr<20]
print("values < 20 : " , filtered)
#معاملات منطقية
s = (arr>10)&(arr<30)
print("boolean s : ",s)
print("Filtered values : " , arr[s])
#العناصر الفريدة
arr2=([40,10,20,10,30,40])
print("unique values : " , np.unique (arr2))
#ترتيب العناصر تصاعديا
print(np.sort(arr2))
#البحث عن الموقع
arr3=np.array([5,10,20,10,50])
indices =np.where(arr3==10)
print(indices[0])
#اكتشاف قيمة مفقودة
arr4=np.array([10.0,np.nan,25.0,np.inf])
print("is NaN : ",np.isnan(arr4))
#اكتشاف قيمة لا نهائية
print("is inf : ",np.isinf(arr4))
#ازالة القيم المفقودة
clean=arr4[~np.isnan(arr4)]
print(clean)

