def dectobin(dec):
    binnum = ""

    if dec ==0:
        return "0"
    while dec>0:
        tempbin = dec%2
        binnum = str(tempbin) + binnum
        dec = dec//2
    print(binnum)
    return binnum
def checkAmountOFblocks(binnum):
    blocks = {"blok_0":0,
            "blok_1":0
            }
    temp = []
    temp2 = []
    asp = ""
    asp1 = ""
    for i in binnum:
        if i=="0":
            asp+="0"
        elif i!="0" and asp!="":
            temp.append(asp)
            asp=""
    for j in binnum:
        if j=="1":
            asp1+="1"
        elif j!="1" and asp1!="":
            temp2.append(asp1)
            asp1=""
    if asp1 !="":
        temp2.append(asp1)
    blocks["blok_0"] = len(temp)
    blocks["blok_1"] = len(temp2)
    blk = blocks["blok_0"] + blocks["blok_1"]
    return blk

ile = 0
with open("../2023maj/Dane_2305/bin_przyklad.txt", "r") as bin:
    for i in bin:
        if checkAmountOFblocks(i[:-1]) <= 2:
            ile+=1
print(ile)
