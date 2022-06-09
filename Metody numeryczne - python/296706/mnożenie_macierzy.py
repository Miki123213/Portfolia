from numpy import matrix
A = [[-1.0,  2.0, -2.0], 
     [ 2.0,  4.0,  1.0],
     [-3.0, -1.0,  2.0]]
    
X = [ 2.0, -1.0, 3.0]


N = len(X)

B = []


for w in range(N):
    b = 0
    for k in range(N):
        b += A[w][k] * X[k]
    B.append(b)
    print
    print "b=", B[w]

print
print B

print matrix(A) * matrix(X)


    