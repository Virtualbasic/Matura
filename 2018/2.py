n = 32
import sys
sys.setrecursionlimit(20000)
#rek
def F(n):
    if n <1 :
        return 0
    elif n <2:
        return 1
    else:
        return F(n-1) + F(n-2)
def fit(n):
    pywyra = (0,1)
    a, b = pywyra
    print(a)
    while n>1:
        a, b = b, a + b
        print(b)
        n-=1
    return b
def Fit(n):
    a, b = 0 ,1
    for i in range(1 , n-1):
        print(b)
        a , b =b , a +b
    return b
def Fw(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n % 2 ==0:
        k = n // 2
        fk = Fw(k)
        fk_one = Fw(k-1)
        print(fk**2 - fk_one*2)
        return fk**2 - fk_one*2
    else:
        k =(n+1)  // 2
        fk = Fw(k)
        fk_one = Fw(k-1)
        print(fk**2 - fk_one*2)
        return fk**2 - fk_one*2
#def grade(grade: list[int])-> int:
#    return sum(grade)/len(grade)
result = Fw(n)
print(result)
