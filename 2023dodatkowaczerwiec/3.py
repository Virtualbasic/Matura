def check(x):
    zrownowazona = False
    prawiezrownowazona = False
    zeros = 0
    ones =  0
    for i in x:
        if int(i)>0:
            ones+=1
        else:
            zeros+=1
    if zeros == ones:
        zrownowazona = True
        print(f"zrownowazona {zrownowazona} ,  prawiezrownowazona {prawiezrownowazona}")
        return 1
    elif zeros == ones-1 or zeros == ones+1:
        print(f"zrownowazona {zrownowazona} ,  prawiezrownowazona {prawiezrownowazona}")
        prawiezrownowazona= True
        return 2


with open("anagram.txt" , "r") as ang:
    z = 0
    pz = 0
    for i in ang:
        if check(i[:-1]) == 1:
            z+=1
        elif check(i[:-1]) == 2:
            pz+=1

print(z  , end=f" {pz}")