# NO DONE YET
def odAB(pkt1, pkt2):
    xone = pkt1[0]
    yone = pkt1[1]
    xtwo = pkt2[0]
    ytwo = pkt2[1]
    return ((xtwo-xone)**2+(xtwo-xone)**2)**0.5
with open("MIN-DANE-2017/punkty.txt" , "r") as pkt:
    x = ""
    y = ""
    pktt = []
    pointsDistance = []
    for i in pkt:
        temptab = [z for z in i if x !='\n']
        x = "".join(temptab[:temptab.index(" ")])
        tt =temptab[temptab.index(" ")::]
        y = "".join([y for y in tt if y !=" " and y!= "\n"])
        pktt.append([int(x),int(y)])
    for i in range(0,len(pktt)):
        for j in range(i+1 , len(pktt)):
            pointsDistance.append([pktt[i], pktt[j], odAB(pktt[i],pktt[j])])
            #print(pktt[i] , end=f"{pktt[j]}")
    biggest = 0
    bx = []
    by = []
    for i in pointsDistance:
        if i[2]  > biggest:
            biggest = i[2]
            bx = i[0]
            by = i[1]
    print(f"{biggest} dla punktów A {bx}  B {by}")
