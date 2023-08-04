A = [5, 99, 3, 7, 111, 13, 4, 24, 4, 8]
def check(some=[]):
    n = len(some)
    w = 0
    for i  in some:
        if i%2==0:
            w=i
            break
    return w

print(check(A))

#1.2 liniowa