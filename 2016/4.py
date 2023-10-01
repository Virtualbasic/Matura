points = []
counter = 0
def toint(c):
    return  int(c)
def checkPoints(tab=[]):
    x = tab[0]
    y = tab[1]
    r = 200
    equation = (x - 200)**2 + (y - 200)**2
    if equation == r**2:
        print(x,y)
def checkIfInTheCircuit(tab=[]):
    x = tab[0]
    y = tab[1]
    r = 200
    equation = (x - 200)**2 + (y - 200)**2
    if equation < r**2:
        return    True
with open("dane/punkty.txt", "r") as point:
    for i in point:
        temp = (i[:-1].split())
        temp2 = list(map(toint, temp))
        checkPoints(temp2)
        if checkIfInTheCircuit(temp2):
            #print(temp2)
            counter+=1
print(counter)


#1
#256 8
#200 400
#2
#7852