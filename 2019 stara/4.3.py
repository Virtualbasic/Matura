Dzialki = []
with open("Dane_PR2/dzialki.txt" , "r") as d:
    tmp =[]
    for i in d:
        if i.isspace():
          Dzialki.append(tmp)
          tmp = []
        else:
            z = i.replace("\n" , "")
            tmp.append(z)
def checkPola(D):
    for i in range(len(D)):
        z = []
        for j in range(len(D[i])):
            z.append(D[i][j])
        D[i] = z
    g = 0
    tmp = []
    while g < 30:
        for i in range(g+1):
            for j in range(g+1):
                tmp.append(D[i][j])
        if "X" in tmp:
            return g
        g+=1
        tmp = []

Pola  = []
for  nr , i in enumerate(Dzialki):
    Pola.append([nr+1, checkPola(i)])
b = 0
handler = []
for i in Pola:
    if i[1] > b:
        b = i[1]
        handler =   [i]
for i in Pola:
    if i[1] == b and i not in handler:
        handler.append(i)
print(handler)




















'''

def znajdz_maksymalny_kwadrat(dzialka):
    N = len(dzialka)  
    maksymalny_bok = 0 

    pierwsza_przeszkoda_wiersz = N
    pierwsza_przeszkoda_kolumna = N

    for i in range(N):
        if pierwsza_przeszkoda_wiersz == N and ('X' in dzialka[0][i] ):
            pierwsza_przeszkoda_wiersz = i
        if pierwsza_przeszkoda_kolumna == N and any(wiersz[i] == 'X'  for wiersz in dzialka):
            pierwsza_przeszkoda_kolumna = i

    maksymalny_bok = min(pierwsza_przeszkoda_wiersz, pierwsza_przeszkoda_kolumna)

    return maksymalny_bok


for index, dzialka in enumerate(Dzialki):
    rozmiar =znajdz_maksymalny_kwadrat(dzialka)
    print(f"Działka {index + 1}: Największy kwadrat ma bok {rozmiar}")

'''


'''
def acline(n):
    i = 0
    tmp = n
    T = []
    if n[0][0] != "X":
        i = 1
    while i < 30:
        for j in range(i):
            for g in range(i):
                if n[g] == "X":
                    T.append(["*"*g])
        i+=1
    print(T)jestem 

print(acline(Dzialki[0]))
'''
'''

def check(n):
    nm = len(n[0])
    for i in n:
        if len(i) < nm:
            return  False
    return  True

def checkV2(n):
    acwart = 0
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            acwart = len(n[i+1])
    return  acwart



WyznaczonePlace = []
nr = 1
for i in Dzialki:
    tmpF = []

    for d in i:
        if d[0]
        accl = ""
        for l in d:
            if l != "X":
                accl +=l
            else:
                tmpF.append(accl)
                accl = ""
                break
        if len(accl) > 0:
            tmpF.append(accl)
    if check(tmpF):
        WyznaczonePlace.append([nr , len(tmpF[0])])
    else:
        WyznaczonePlace.append([nr, checkV2(tmpF)])
    nr +=1
print(WyznaczonePlace)

'''

