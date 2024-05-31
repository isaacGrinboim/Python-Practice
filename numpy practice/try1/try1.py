import numpy as np

A = np.matrix('1 2; 7 4')
B = A.getI()
print(A*B)
C = np.random.randint(3,4, 2)
print(C)
print(A.dtype)
print(C.dtype)

arr = np.arange(1,10)
arr2 = arr.reshape(9,1)
print(arr2)

print(arr2.shape)
