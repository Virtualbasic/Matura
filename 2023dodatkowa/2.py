'''
testcase = "mascarpone"
suffix = []
for  i in range(0 , len(testcase)):
    suffix.append(testcase[i:])
print(sorted(suffix))
'''
def czymniejsze(n,s,k1,k2):
    i = k1
    j = k2
    while i<=n and j<=n:
        if s[i] == s[j]:
            i = i +1
            j = j +1
        elif s[i] < s[j]:
            return  False
        else:
            return True
    if j<=n:
        return True
    else:
        return  False


with open("DANE/DANE_M/slowa1.txt" , "r") as charact:
    temp = [j[:-1] for j in charact]
    temp[2] = [int(i) for i in temp[2] if i.isnumeric()]
    temp[0] = int(temp[0])
print(f"{temp[0]} , {temp[1]} , {temp[2][0]} , {temp[2][1]}")
print(czymniejsze(temp[0] , temp[1] , temp[2][0] , temp[2][1]))
#print(czymniejsze(len("kalafiorowa") ,"kalafiorowa", ))
