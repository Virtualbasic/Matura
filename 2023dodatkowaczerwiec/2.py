def czymniejszy(n,s,k1,k2):
    i = k1
    j = k2
    while i <= n and j <= n:
        if s[i-1] == s[j-1]:
            i += 1
            j += 1
        else:
            if s[i] < s[j]:
                return True
            else:
                return  False
    if j <= n:
        return  True
    else:
        return  False
#2.1  aaaaaaaaaa  1, 3
#2.2
'''
True slowa1.txt 
False slowa2.txt 
False slowa3.txt 
'''
tab = ["slowa1.txt","slowa2.txt","slowa3.txt"]
for i in tab:
    with open(i , "r") as sufiks:
        conf = []
        for j in sufiks:
            conf.append(j[:-1].split())
        print(czymniejszy(int(conf[0][0]), conf[1][0], int(conf[2][0]), int(conf[2][1]) ) , end = f" {i} \n")
