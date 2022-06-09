from numpy import matrix, dot

A = [[ 5.0,  1.0, -3.0],
     [ 1.0,  4.0,  1.0],
     [-2.0,  1.0, -5.0]]

B = [-2.0, 12.0, -15.0]

X = [1.0, 1.0, 1.0]

N = len(B)

D = 1.0e-9

def Jacob(a, b, x):
    r = []
    for w in range(N):
        s = 0
        for k in range(N):
            if(w != k):
                s += a[w][k] * x[k]
        r.append((b[w] - s)/a[w][w])
    return r
    
def GaussS(a, b):
    for w in range(N):
        s = 0
        for k in range(N):
            if(w != k):
                s += a[w][k] * X[k]
        X[w] = (b[w] - s)/a[w][w]
    return X


i = 0
while True:
    i += 1
    P = list(X)
#    X = Jacob(A, B, X)
    X = GaussS(A, B)
    print i, X
    if abs(P[0] - X[0]) < D and \
       abs(P[1] - X[1]) < D and \
       abs(P[2] - X[2]) < D: break

print dot(matrix(A), X)
print B

"""
for i in range(10):
    X = GaussS(A, B)
    print i, X
"""