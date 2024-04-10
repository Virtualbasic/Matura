pi = [i[:-1] for i in open("Dane_2305/pi.txt" , "r")]
zal =[]
for i in range(len(pi)-1):
    if int(pi[i] + pi[i+1]) > 90:
        zal.append(int(pi[i] + pi[i+1]))

print(len(zal))