def checkblocks(num):
    def DectoBin(x):
        b = ''
        while x > 0:
            if x % 2 == 0:
                b += "0"
            else:
                b += "1"
            x = x // 2
        return b[::-1]

    b1 = 0
    b0 = 0
    #x = 245
    d = 0
    z = num
    for g in num:
        d += 1

    start = z[0]
    if start == "0":
        b0 += 1
    elif start == "1":
        b1 += 1
    for i in range(d - 1):
        if z[i + 1] != start:
            start = z[i + 1]
            if z[i + 1] == "1":
                b1 += 1
            else:
                b0 += 1
    if b1 + b0<=2:
        return True

binnums = [i[:-1] for i in open("Dane_2305/bin_przyklad.txt" , "r")]

warunek =  0

def bintodec(x):
    p = 0
    num = 0
    for i in x:
        if i =="1":
            num+= 2**p
        p+=1
    return  num



biggestnum = [0, ""]
for i in binnums:
    if bintodec(i) > biggestnum[0]:
        biggestnum = [bintodec(i) , i]
    if checkblocks(i):
        warunek+=1

print(warunek)

print(biggestnum)