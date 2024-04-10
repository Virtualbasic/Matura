def TestF(k):
    PP = 1
    if k < 2:
        return  False
    for a in range(2,k):
        if (a**k)%k!=a:
            PP = 0
    return  PP
def jestWzgledniePierwszy(a, b):
    while b != 0:
        a, b = b, a % b
    return a == 1

def czyLC(k):
    if k <= 2 or TestF(k):
        return 0

    for i in range(2, k):
        if jestWzgledniePierwszy(i, k):
            if pow(i, k-1, k) != 1:
                return 0
    return 1
