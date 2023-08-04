def sym(a,b):
    cnt = 0
    def slt(a, b):
        nonlocal cnt
        if a!=0:
            slt(a-1,b+1)
            print(a*b)
            cnt+=1
            slt(a-1, b+1)
    slt(a,b)
    return cnt
print(sym(10,2020))

#2.1
#przypadek pierwszy
#5859585
#przypadek drugi
#464646444646464
#2.2
#31
#63
#1023