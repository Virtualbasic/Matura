def dectobin(x):
    bin = ""
    while x>0:
        if x%2 == 0:
            bin+="0"
        else:
            bin+="1"
        x//=2
    return  bin[::-1]


b = dectobin(123)
a = "101101"
c =  dectobin(int("2D" , 16))


while len(a)< len(b):
    a += "0"
    c += "0"
a =a[::-1]
c = c[::-1]
#print(a)


def XOR(n1 , n2):
    if n1>n2:
        z = ""
        g = len(n2)
        while len(n1) != g:
            z+="0"
            g+=1
        n2 = z+n2
    else:
        z = ""
        g = len(n1)
        while len(n1) != g:
            z += "0"
            g += 1
        n1 = z + n1


    result = ""
    for i in range(len(n1)):
        if n1[i] == "1" and n1[i]==n2[i]:
            result+="0"
        elif  n1[i] == "1" and n2[i]=="0" or n1[i] == "0" and n2[i]=="1":
            result+="1"
        else:
            result+="0"
    return  result


#print(int( XOR(XOR(b, a), c) , 2) )
data = [i[:-1] for i in open("Dane_2305/bin.txt")]

for i in data:
    p = i
    q = dectobin(int(float(int(i,2)//2)))
    print(XOR(p,q))



