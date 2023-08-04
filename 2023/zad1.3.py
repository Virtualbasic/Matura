def checkSubstring(str):
    for j in str:
        if j != ".":
            return False
    return True

def checkingLines(line):
    global białeSzach
    global czarneSzach
    szach = ""
    findk = 0
    findW = 0
    if "k" in line and "W" in line:
        findk = line.find("k")
        findW = line.find("W")
        szach = " białe szachują czarne"

    elif "K" in line and "w" in line:
        findk = line.find("K")
        findW = line.find("w")
        szach = " czarne szachują białe "


    substr = ""
    if findk > findW:
        substr = line[findW + 1:findk]
        if checkSubstring(substr):
            #print(line[findW])
            #print(substr)
            #print(szach)
            if line[findW] == "W":
                białeSzach+=1
            else:
                czarneSzach+=1
    elif findk < findW:
        substr = line[findk + 1:findW]
        if checkSubstring(substr):
            #print(line[findW])
            #print(substr)
            #print(szach)
            if line[findW] == "W":
                białeSzach+=1
            else:
                czarneSzach+=1
    #f = open("noreson.txt" , "w")
    #f.write(szach)
    #f.close()

def checkIfonlyTowerAndKing(plate):
    lines = plate.split("\n")

    columns =[]
    liness = []
    plnasz = ["K", "k", "W", "w", "."]
    col = ""
    for lin in lines:
        liness.append(lin)
    for i in range(len(lines[0])):
        column = [line[i] for line in lines]

        for j in column:
            if j in plnasz:
                col+=j
            else:
                col = ""
                break
        columns.append(col)

        col=""
    for g in columns:
        checkingLines(g)

    for lina in liness:
        checkingLines(lina)
with open("Dane_2203/szachy.txt", "r") as bierka:
    chessboards = bierka.read().strip().split("\n\n")
białeSzach = 0
czarneSzach = 0

for chessboard in chessboards:
    #print(chessboard)
    checkIfonlyTowerAndKing(chessboard)

print("białe szach ", end=str(białeSzach)  + "\n")
print("czarne szach ", end =str(czarneSzach))
