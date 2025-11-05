# x = [column for column in range(3)]
# matrix = [[column for column in range(3)] for row in range(3)]
# matrix[0][0] = 10
# print(matrix)
# print(x)

import numpy as np

A = [[1,2],[[3,4]]]
B = [[5,6],[[7,8]]]
C = np.linalg.inv(A)
print(np.dot(A,B))