import numpy as np
#تنظيف البيانات
arr=np.array([22.5,24.0,np.nan,19.8,np.nan,26.3,21.0])
print(np.isnan(arr))
clean=arr[~np.isnan(arr)]
print(clean)
print(np.mean(clean