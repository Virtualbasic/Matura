p1 = []
p2 = []

with open("dane/NM_DANE_PR/przyklad1.txt", "r") as f:
    for line in f:
        lin = line[:-1].split()
        p1.append(int(lin[-1]))
with open("dane/NM_DANE_PR/przyklad2.txt", "r") as r:
    for line in r:
        lan =line[:-1].split()
        p2.append(int(lan[-1]))



print(p2,p1)
counter = 0
for i in p1:
    for j in p2:
        if i == j:
            counter+=1
print(counter)
