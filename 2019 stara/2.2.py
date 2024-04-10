def TestF(k):
    PP = 1
    if k < 2:
        return  False
    for a in range(2,k):
        if (a**k)%k!=a:
            PP = 0
    return  PP

print(TestF(6))
