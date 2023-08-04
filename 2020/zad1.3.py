A = [1, 2, 3, 4, 5]
B = [3, 4, 5, 1, 2]

def czy_podobne(a =[], b=[] ):
    n = len(a)
    k= 0
    for i in range(0 ,n):
        if a[:i] == b[n-i:] and a[i:] == b[:n-i]:
            print(a[:i], b[n-i:])
            k=i
    if k>0:
        return k , True
    else:
        return False
print(czy_podobne(A,B))
