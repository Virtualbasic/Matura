testline = "k.....W."

def checkSubstring(str):
    for j in str:
        if j != ".":
            return False
    return True
def checkingLines(line):
    findk = 0
    findW = 0
    szach = ""
    if "k" in line and "W" in line:
        findk = line.find("k")
        findW = line.find("W")
        szach = " czarne szachują białe"
    elif "K" in line and "w" in line:
        findk = line.find("K")
        findW = line.find("w")
        szach = " białe szachują czarne"


    substr = ""
    if findk > findW:
        substr = line[findW + 1:findk]
        if checkSubstring(substr):
            print(substr)
            print(szach)

    elif findk < findW:
        substr = line[findk + 1:findW]
        if checkSubstring(substr):
            print(substr)
            print(szach)



checkingLines(testline)