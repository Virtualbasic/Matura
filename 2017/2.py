x =  13
def licz(x):
    if x == 1:
        return  1
    else:
        w = licz(x // 2)
        print("|")
        if x%2 == 1:
            return w +1
        else:
            return  w -1
print(licz(x))

'''
13 = 2
21 = 1
32 = -4 
'''