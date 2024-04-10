def alg(n):
    dl = []
    accs = 0
    for i in range(n,0,-1):
        if i**2 <n :
            accs+=i**2
            if accs<=n:
                dl.append(i)
            else:
                accs-=i**2
    accurate = 0
    for g in dl:
        accurate+=g**2
    while accurate<n:
        dl.append(1)
        accurate+=1
    print(dl)
    return len(dl)

print(alg(32))