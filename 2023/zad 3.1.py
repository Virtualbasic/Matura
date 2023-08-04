def modulo(a,x,M):
    b = (a**x)%M
    return b


x = 0
g= 5 #insert b
for i in range(1,100):
    x+=1
    if modulo(2,x,59) == g:
        print(x)
        break
print(modulo(9,2,80))


#b=5
#M=2
#x=6
#b=1