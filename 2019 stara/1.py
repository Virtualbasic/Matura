TablicaA = [1,2,7,3,1,4,6,7]

def zad(A):
    n = len(A)
    C= [1]*n
    for i in range(1,n):
        for j in range(0,i):
            if A[j]<A[i] and C[j] +1 > C[i]:
                C[i] = C[j]+1
    return C

print(zad(TablicaA))



#1.3
#[1,2,7,3,1,4,6,7]
