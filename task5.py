import numpy as np
#البحث والشروط
prices = np.array([15,45,25,120,45,60])
print(np.where(prices==45))
indices =np.where(prices==45)
print(indices[0])
#استخراج المنتجات التي يتراوح سعرها بين ٢٠و٩٠ 
print(prices[(prices>20) & (prices < 90)])
#الاسعار الفريدة
print(np.unique(prices))
