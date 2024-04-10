def bin(n):
    b =""
    while n > 0:
        r= n%2
        b+= str(r)
        n = n //2
    return b[::-1]
print(bin(30))
T = []
with open("anagram.txt" , "r") as bn:
    for i in bn:
        T.append(i[:-1])

b =0
for i in range(len(T)-1):
    if (int(T[i], 2) - int(T[i+1] ,2 )) *-1 >b:
        b =(int(T[i], 2) - int(T[i+1] ,2 )) *-1

print(bin(b))
