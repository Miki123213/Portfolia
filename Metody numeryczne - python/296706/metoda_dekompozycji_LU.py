from scipy.linalg import lu_factor, lu_solve, lu
from pprint import pprint


A = [[-1.0,  2.0, -3.0,  1.0,  2.0],
     [ 1.0, -3.0,  1.0, -2.0,  4.0],
     [-2.0,  3.0, -1.0,  4.0, -2.0],
     [ 4.0, -2.0, -3.0,  1.0, -1.0],
     [-3.0, -1.0, -2.0,  1.0,  4.0]]
     
B = [8.0, 10.0, 7, -10.0, 13.0]

LU = lu_factor(A)

X = lu_solve(LU, B)

print X
#print 2*1.7278481 - 3*3.07974684 + 4.08227848 + 2*4.85063291
pprint(LU)
print
pprint(A)
print
P, L, U = lu(A)
pprint(P)
print
pprint(L)
print
pprint(U)

