p1 = []
p2 = []
parzystep1=[]
parzystep2=[]
with open("dane/NM_DANE_PR/przyklad1.txt", "r") as f:
    for line in f:
        lin = line.split()
        cparzyste=0
        for i in lin:
            if int(i)%2 == 0:
                cparzyste+=1
        parzystep1.append(cparzyste)
        cparzyste = 0
        p1.append(lin)
with open("dane/NM_DANE_PR/przyklad2.txt", "r") as r:
    for line in r:
        lan =line.split()
        cparzyste = 0
        for i in lan:
            if int(i) % 2 == 0:
                cparzyste += 1
        parzystep2.append(cparzyste)
        cparzyste = 0
        p2.append(lan)
print(parzystep1,parzystep2)
for i in range(0,4):
        if parzystep1[i] == parzystep2[i]:
            print("found")



