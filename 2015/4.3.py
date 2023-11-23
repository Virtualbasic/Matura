def conw(num):
    dec= 0
    for i in range(len(num)):
        digit = int(num[i])
        dec += digit*2**(len(num) -i-1)
    return dec
with open("Dane_PR/liczby.txt" , "r") as nums:
    tab =[]
    row = 0
    for i in nums:
        tab.append([conw(i[:-1]) , row+1 , i[:-1]])
        row +=1
print(tab)
biggest  = 0
row =  0
rowmin = 0
binnum = ''
binnummin = ''
min = tab[0][0]
for i in range(0 , len(tab)):
    if tab[i][0]>biggest:
        biggest = tab[i][0]
        row = tab[i][1]
        binnum = tab[i][2]
    if tab[i][0] < min:
        min = tab[i][0]
        rowmin = tab[i][1]
        binnummin = tab[i][2]
print(f"the biggest value {biggest} on  row {row} for bin num {binnum}")
print(f"the smalest value {min} on  row {rowmin} for bin num {binnummin}")