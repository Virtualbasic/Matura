def pota(a,k):
    if a<2 or a > k:
        return  False
    return  (a**k)%k

print(pota(3,12))