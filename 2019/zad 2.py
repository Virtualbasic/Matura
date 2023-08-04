def pisz(s,n,k):
    if len(s) == n:
        print(s)
    else:
        for i in range(0 , k):
            pisz(s + str(i), n ,k)
pisz("", 2, 2)
#a
#00
#01
#10
#11
#b
# 1. pisz("10",2,2) , 2. pisz("11",2,2) # k0+...kn

#zad 2.2
#000  8
#001
#010
#011
#100
#101
#110
#111

#00   9
#01
#02
#10
#11
#12
#20
#21
#22


