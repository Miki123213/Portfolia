
A = [[-1.0,  2.0, -2.0], 
     [ 2.0,  4.0,  1.0],
     [-3.0, -1.0,  2.0]]

B = [-10.0, 3.0, 1.0]

N = len(B)

X = range(N)

def pmac(m):
    w = len(m)
    k = len(m[0])
    for i in range(w):
        print "[",
        for j in range(k):
            print "%6.2f" % m[i][j],
        print "]"
    print
    
print "A="
pmac(A)

AB = []
for w, x in zip(A, B):
    AB.append(w+[x])

print "A!B="
pmac(AB)

for K in range(N-1):
    for w in range(K+1, N):
        p = AB[w][K] / AB[K][K]
        for k in range(N+1):
            AB[w][k] = AB[w][k] - p * AB[K][k]
            
print "(A!B)' ="
pmac(AB)

n = range(0, N)
n = n[:: -1]

for w in n:
    s = 0
    for k in range(w+1, N):
        s += AB[w][k] * X[k]
    
    X[w] = (AB[w][N] - s) / AB[w][w]

print "X=", X
