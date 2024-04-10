def bintodec(bin):
    decnum = 0
    bincounter = 0
    for num in bin[::-1]:
        if num=="1":
            decnum+=2**bincounter
        bincounter+=1
    return decnum
def dectobin(dec):
    binnum = ""

    if dec ==0:
        return "0"
    while dec>0:
        tempbin = dec%2
        binnum = str(tempbin) + binnum
        dec = dec//2

    return binnum
def operat(p):
    decsec  = bintodec(p)
    first = p
    second = dectobin(decsec//2)
    if dec

with open("../2023maj/Dane_2305/bin_przyklad.txt", "r") as operation:
    for i in operation:
