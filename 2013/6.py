numbers = [i[:-1] for i in open("Dane/dane.txt" , "r")]
#a)
warunekA = []
for i in numbers:
    if i[0] == i[-1]:
        warunekA.append(i)
print(warunekA)
print(len(warunekA))
#b)
warunekB = []
for i in numbers:
    i = str(int(i,8))
    if i[0] == i[-1]:
        warunekB.append(i)
print(warunekB)
print(len(warunekB))
#c)
warunekC = []
for i in numbers:
    f =False
    for g in range(len(i)-1 ):
        if int(i[g]) > int(i[g+1]):
            f =True
            break
    if not f:
        warunekC.append(i)
print(warunekC)
print(len(warunekC))