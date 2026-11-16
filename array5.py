import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(arr)
print("\n")
print(arr[0:2])
print("\n")
print(arr[:, 0:2])
print("\n")
print(arr[0:2, 1:3])
print("\n")
print(arr[::2, ::2])
print("\n")
print(arr[::-1])
print("\n")
print(arr[::-2])
print("\n")
arr1= np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print(arr1)
print("\n")
print(arr[:, :, 0:2])
print("\n")