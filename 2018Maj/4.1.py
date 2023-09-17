forsyg = []
with open("Dane_PR/przyklad.txt" , "r") as f:
    for  i in f:
        forsyg.append(i[:-1])
haslo = ""
for i in range(39,len(forsyg),40):
    haslo+=forsyg[i][-1:]
print(haslo)