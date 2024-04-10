mecz = [i for i in open("Dane_2212/mecz_przyklad.txt" , "r")]
w = 0
w2 = 0
wA = 0
wB = 0
for i in range(len(mecz[0])-1):
    if mecz[0][i] =="A":
        wA+=1
    else:
        wB +=1
    if mecz[0][i+1]!=mecz[0][i]:
        w+=1
    if wA >=1000 and wB<=wA-3 or (wB >=1000 and wA<=wB-3):
        if wA > wB:
            print(f"rozgrywke wygrała drużyna A {wA} a B miała {wB}")
            break
        else:
            print(f"rozgrywke wygrała drużyna B {wB} a A miała {wA}")


print(w)



