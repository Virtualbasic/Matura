def bintodec(bin):
    decnum = 0
    bincounter = 0
    for num in bin[::-1]:
        if num=="1":
            decnum+=2**bincounter
        bincounter+=1
    return decnum

binnums =[]
with open("../2023maj/Dane_2305/bin.txt", "r") as binnum:
    index = 0
    for i in binnum:
        binnums.append([bintodec(i[:-1]) , i[:-1] ,index])
        index+=1
print(binnums)
bigest  =  0
handler = []
for i in range(0,len(binnums)):
    if binnums[i][0] > bigest:
        bigest = binnums[i][0]
        handler = binnums[i]
print(handler)
