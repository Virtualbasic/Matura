def countzeros(str):
    zeros = 0
    ones = 0
    for i in str:
        if i == "0":
            zeros+=1
        else:
            ones+= 1
    if zeros> ones:
        print(zeros , end=f" {ones}  ")
        return  True
    return  False

with open("Dane_PR/liczby.txt" , "r") as num:
    count = 0
    for i in num:
        if countzeros(i[::-1]):
            print(i)
            count+=1
    print(count)

#390
