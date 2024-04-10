mecz = [i for i in open("Dane_2212/mecz.txt" , "r")]
passaA = []
passaB = []
accA = 0
accB = 0
tmp = ""
znak = mecz[0][0]
for i in range(len(mecz[0])):
    if mecz[0][i] ==znak:
        tmp +=znak
    else:
        if len(tmp)> 10 and tmp[0] =="A":
            passaA.append(len(tmp))
        elif len(tmp)> 10 :
            passaB.append(len(tmp))
        tmp=znak
        znak = mecz[0][i]
print(passaA)
print(passaB)