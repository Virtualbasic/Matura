def DectoBin(x):
    b = ''
    while x>0:
        if x%2 ==0:
            b+="0"
        else:
            b+="1"
        x= x//2
    return  b[::-1]

b1= 0
b0 = 0
x= 245
d = 0
z = DectoBin(x)
for g in DectoBin(x):
    d+=1

start = z[0]
if start == "0":
    b0 += 1
elif start == "1":
    b1 += 1
for i in range(d-1):
    if z[i+1] != start:
        start = z[i+1]
        if z[i+1] == "1":
            b1+=1
        else:
            b0+=1

print(f" bloki jedynek {b1}  bloki zer {b0}")




