Fordane1 = []
Fordane2 = []
fnumber = []
fnumber2 = []
with open("dane/NM_DANE_PR/przyklad1.txt", "r") as f:
    for i in f:
        Fordane1.append(i[:-1].split())
with open("dane/NM_DANE_PR/przyklad2.txt", "r") as f:
    for i in f:
        Fordane2.append(i[:-1].split())
def inter(n):
    return  int(n)

for j in Fordane2:
    checkCHars = [i for i in j]
    intchechars = map(inter , checkCHars)
    snm = list(intchechars)
    fnumber2.append(snm)
for j in Fordane1:
    checkCHars = [i for i in j]
    intchechars = map(inter , checkCHars)
    snm = list(intchechars)
    fnumber.append(snm)

n = 0
while n < len(fnumber)  :
    same = all(item in fnumber[n] for item in fnumber2[n])
    if same:
        print("found" + " " + "wers %s"%(n+1) )
    #if sorted(fnumber[n]) == sorted(fnumber2[n]):
    #    print("Found")
    #print(sorted(fnumber[n]))
    n+=1
print(fnumber)
# thats is fucking overthink nuts
#n = 0
#wyst = 0
#while n<5:
#    counter = 0
#    for i in range(0,4):
#        for j in range(0,10):
#            if fnumber[i][j] in fnumber2[i] and fnumber2[i][j] in fnumber[i]:
#                print(fnumber[i][j],fnumber2[i] )
#                counter+=1
#        if counter == 10:
#            wyst+=1
#            print("found")
#        else:
#            print("not found ")
#    n+=1

