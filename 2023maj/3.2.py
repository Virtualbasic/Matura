pi = [i[:-1] for i in open("Dane_2305/pi.txt" , "r")]
zal = {}
for i in range(0,100):
    if len(str(i)) < 2:
        zal["0"+str(i) ] = 0
    else:
        zal[str(i)] = 0

for i in range(len(pi)-1):
    if pi[i] + pi[i+1] in zal:
        zal[pi[i] + pi[i+1]] +=1
big= 0
ss = []
smal = zal.get("00")
b = []
s =[]

for k, v in zal.items():
    if v > big:
        b= [k,v]
        big = v
    if v < smal or v == smal:
        ss.append([k,v])
        s = [k,v]
        smal = v


print(b)
print(ss[0])
