def fromBinToDec(num):
    decnum = 0
    for i in range(len(num)):
        digit = int(num[i])
        decnum += digit*2**(len(num)-i-1)
    if decnum % 8 == 0 and decnum % 2 == 0:
        print("podzielne 8")
        return 3
    if decnum % 8 == 0:
        print("podzielne 8")
        return 2
    if decnum % 2==0:
        print("podzielne 2 ")
        return 1
with open("Dane_PR/liczby.txt") as num:
    devideight = 0
    devidetwo = 0
    for i in num:
        if fromBinToDec(i[:-1]) == 1:
            devidetwo +=1
        elif fromBinToDec(i[:-1]) == 2:
            devideight+=1
        elif fromBinToDec(i[:-1]) == 3:
            devidetwo += 1
            devideight += 1

    print(f"devideeight {devideight}", end=f" devide two {devidetwo}")
