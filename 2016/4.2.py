points = []
nk = 0
n = 0
def toint(c):
    return  int(c)
def checkIfInTheCircuit(tab=[]):
    x = tab[0]
    y = tab[1]
    r = 200
    equation = (x - 200)**2 + (y - 200)**2
    if equation <= r**2:
        return    True
with open("dane/punktytest.txt", "r") as point:
    for i in point:
        temp = (i[:-1].split())
        temp2 = list(map(toint, temp))
        if checkIfInTheCircuit(temp2):
            nk+=1
        else:
            n+=1

r = 200
P = 400*400

pi = 4 * (nk / 100)

print(pi)
