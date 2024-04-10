import  copy
pierwszePokolenie  = [i for i in  open("dane/gra.txt")]
for v in range(len(pierwszePokolenie)):
    pierwszePokolenie[v] = [j for j in pierwszePokolenie[v] if j !="\n"]
pokolenie = 37
i = 2

def komorkaCheck(n):
    L = [2,3]
    nowepokolenie = copy.deepcopy(n)
    for ln  in range(1,len(n)-1):
        for l in range(1 ,len(n[ln])-1):
             ampulka = [n[ln][l-1] ,n[ln][l+1], # komórki w tym samym wierszu obok komórki
                        n[ln-1][l],n[ln+1][l], # komórki nad i pod aktualną komórką
                        n[ln-1][l-1], n[ln-1][l+1] ,  #komórki na skos  u góry
                        n[ln+1][l-1], n[ln+1][l+1]]#komórki na skos  na dole  góry
             zywi = 0
             for z in ampulka:
                 if z == "X":
                     zywi += 1
             if n[ln][l]  == "." and zywi == 3:
                 nowepokolenie[ln][l] = "X"
             elif n[ln][l]  == "X" and zywi in L:
                     pass
             elif n[ln][l]  == "X" and zywi not in L:
                 nowepokolenie[ln][l] = "."
             else:
                 nowepokolenie[ln][l] = "."
    ampulki = [
        #ampulkakgl
         [
            n[-1][0], n[1][0],
            n[0][-1] , n[0][1],
            n[1][1], n[1][-1],
            n[-1][1], n[-1][-1]
         ],
        #ampulkakgp
         [
            n[-1][-1], n[1][-1],
            n[0][0], n[0][-2],
            n[1][-2], n[1][0],
            n[-1][-2], n[-1][0]
         ],
        #ampulkakdl
         [
            n[-2][0], n[0][0],
            n[-1][-1], n[-1][1],
            n[-2][1], n[-1][-1],
            n[0][1], n[0][-1]
         ],
        #ampulkakdp
         [
            n[-2][-1], n[0][-1],
            n[-1][-2], n[-1][0],
            n[-2][-1], n[-2][0],
            n[0][-2], n[0][0]
         ]
    ]
    holder = [[0,0], [0,-1], [-1,0], [-1,-1]]
    indeksy = [n[0][0] , n[0][-1], n[-1][0] , n[-1][-1]]
    for g in range(len(holder)):
        zz = 0
        for k in ampulki[g]:
            if k == "X":
                zz +=1
        if indeksy[g] == "X" and zz in L:
            nowepokolenie[holder[g][0]][holder[g][1]] = "X"
        elif indeksy[g] == "." and zz == 3:
            nowepokolenie[holder[g][0]][holder[g][1]] = "X"
        else:
            nowepokolenie[holder[g][0]][holder[g][1]] = "."
    for i in range(1,len(n)-2):
        ampulkalewa = [
            n[i-1][0], n[i+1][0],
            n[i][-1] , n [i][1],
            n[i+1][1], n[i+1][-1],
            n[i-1][1], n[i-1][-1]
        ]
        ampulkaprawa = [
            n[i-1][-1], n[i+1][-1],
            n[i][-2] ,  n[i][0],
            n[i+1][-2],  n[i+1][0],
            n[i-1][-2],  n[i-1][0]
        ]
        zzz = [0 , 0]
        for q in ampulkaprawa:
            if q == "X":
                zzz[0]+=1
        for qq in ampulkalewa:
            if qq == "X":
                zzz[1]+=1
        if n[i][0] == "X" and zzz[1] in L:
            nowepokolenie[i][0] = "X"
        elif n[i][0] == "." and zzz[1] == 3:
            nowepokolenie[i][0] = "X"
        else:
            nowepokolenie[i][0] = "."
        if n[i][-1] == "X" and zzz[0] in L:
            nowepokolenie[i][-1] = "X"
        elif n[i][-1] == "." and zzz[0] == 3:
            nowepokolenie[i][-1] = "X"
        else:
            nowepokolenie[i][-1] = "."
    return  nowepokolenie

P = open("dane/gra.txt" , "w")

np = komorkaCheck(pierwszePokolenie)
#for y in np:
        #print(''.join(y))
#        P.write(''.join(y)+"\n")
while i <= 2:
    np = komorkaCheck(np)
    P.write("------------\n")
    P.write(f"numer pokolenia {i}\n")
    for y in np:
         #print(''.join(y))
         P.write(''.join(y)+"\n")
    i+=1
#print(pierwszePokolenie)