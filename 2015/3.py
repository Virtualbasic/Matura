def NWD(a,b):
    while b >0:
        r = a%b
        a = b
        b = r

    return a

print(NWD(12,3))