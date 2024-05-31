import numpy as np  


def orthonormal_matrix(n):
    random_matrix = np.random.rand(n, n)
    Q , _ = np.linalg.qr(random_matrix) #Q , R
    return Q
# x = np.eye(6) #'eye' sounds similar to 'I'
# print (x)


# create numpy 2d-array
m = np.array([[1, 2 , 3 , 4, 5],
              [0, -2 , 134 , 131, 15],
              [0, 0, 11 , 1, 34],
              [0, 0, 0, -101, 56],
              [0 ,0 ,0 ,0 , 93]])

U = np.full((2,2,2),2)
# print("Printing the Original square array:\n", m)
# w = np.linalg.eigvals(m)
# print("eigen values of m: " , w)
# mtm = m.T*m
# w = np.linalg.eigvals(mtm)
# print("eigen values of mtm: " , w)


print(U.dtype)