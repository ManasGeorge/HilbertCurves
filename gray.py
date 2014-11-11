from math import log

def gc(i):
    return i ^ (i / 2)

def gci(g):
    m = 0 if g == 0 else (int)(log(g,2)+1)
    i,j = g,1
    while j < m:
        i = i ^ (g >> j)
        j = j+1
    return i

def g(i):
    count = 0
    while i % 2 == 1:
        i = i/2
        count = count + 1 
    return count

def diff(i,n):
    if i == 0:
        return 0
    if i % 2 == 0:
        return g(i-1) % n
    if i % 2 == 1:
        return g(i) % n

def entry(i):
    if i == 0:
        return 0
    # Integer division
    return gc(2*((i-1)/2))

def transform(e,d,b,n):
    return rotr(b^e,d+1,n)

def inverseTransform(e,d,b,n):
    return rotl(b,d+1,n)^e

def rotl(x,i,n):
    mask = (1 << n) - 1
    return mask & ((x << i) | (x >> (n-i)))

def rotr(x,i,n):
    mask = (1 << i) - 1
    over = ((mask & x) << (n-i))
    return  ((x >> i) | over)

def bit(p,i):
    return (int)((p & (2**i)) > 0)

# Finds the hilbert index h of a point p in n-space, represented as a binary
# number of precision m bits
def hilbertIndex(n,m,p):
    h,e,d = 0,0,0
    for i in range(m-1,-1,-1):
        l = [bit(pi,i) for pi in p]
        l = sum([l[-j-1] * (2**j) for j in range(n)])
        l = transform(e,d,l,n)
        w = gci(l)
        e = e ^ (rotl(entry(w),(d+1),n))
        d = (d + diff(w,n) + 1) % n
        h = (h << n) ^ w
        # print e,d,h
    return h

# Finds the coordinates of the point in n-space with the Hilbert index h
def hilbertIndexInverse(n,m,h):
    e,d = 0,0
    p = [0]*n
    for i in range(m-1,-1,-1):
        w = [bit(h,i*n + j) for j in range(n)]
        w = sum([w[j] * (2**j) for j in range(n)])
        l = gc(w)
        l = inverseTransform(e,d,l,n)
        for j in range(n):
            if bit(p[j],i) == 1:
                p[j] = p[j] & (bit(l,j) << i)
            else:
                p[j] = p[j] | (bit(l,j) << i)
        e = e ^ (rotl(entry(w), d+1, n))
        d = (d + diff(w,n) + 1) % n
    return p
