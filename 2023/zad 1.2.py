
def calc(board):
    global data3
    global amount_of_pieces
    lines = board.split("\n")
    #print(lines)
    BierkiMałe = []
    BierkiDuże = []
    tempBierki = []

    BierkiValue = {
        "w":5,
        "s":3,
        "g":3,
        "h":9,
        "k":1,
        "p":1
    }

    Bduże = 0
    Bmałe= 0
    for i in range(len(lines[0])):
        column = [line[i] for line in lines]
        for j in column:
            if j != ".":
                if j.isupper():
                    BierkiDuże.append(j)
                else:
                    BierkiMałe.append(j)
    for g in BierkiDuże:
        tempBierki.append(g.lower())
    for B in  tempBierki:
        if B in BierkiValue:
            Bduże+=BierkiValue[B]
    for b in BierkiMałe:
        if b in BierkiValue:
            Bmałe+=BierkiValue[b]
    if Bmałe == Bduże:
        #print("equal" + str(Bduże) + str(Bmałe))
        amount_of_pieces.append(len(BierkiMałe) + len(BierkiDuże))
        some = f"equal D{Bduże} M{Bmałe}"
        data3.append(some)

    else:
        print("")
    #print(data3)
    return  Bduże,Bmałe
    #if BierkiMałe.sort() == tempBierki.sort():
    #    print(BierkiMałe,tempBierki)
    #    print("yes")
    #return BierkiDuże, BierkiMałe
f = open("zad1.2Data.txt", "r+")
#print(len(data3))
data3 = []
amount_of_pieces = []


with open("Dane_2203/szachy.txt", "r+") as place:
    boards = place.read().strip().split("\n\n")

for bord in boards:
    print(calc(bord))
smalest = amount_of_pieces[0]
print(amount_of_pieces)
for i in amount_of_pieces:
    if i<=smalest :
        smalest =i
print(smalest)
f.write(str(len(data3)) + " " + str(smalest))