from scipy.linalg import solve, inv
from numpy import dot, matrix

A = [[ 5.0,  1.0, -30.0],
     [ 10.0,  4.0,  1.0],
     [-20.0,  1.0, -5.0]]

B = [-2.0, 12.0, -15.0]

X = solve(A,B)
print X

A1 = inv(A)
X = dot(A1, B)
print X

print dot(matrix(A), X)