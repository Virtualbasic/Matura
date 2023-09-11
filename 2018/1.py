#T = [i for i in range(0,111)]
T = [3,5,7,8,90,13,33,37,40,43]
print(T)
x = 43

def F(x,T=[]):
    p = 1
    forp = 0
    fork = 0
    k = len(T)
    counter = 0
    while p <=k:
        counter+=1
        s = (p+k)//2

        if T[s] == x:
            return True,fork, forp, counter
            break
        elif T[s] < x:
            p = s +1
            forp +=1
        else:
            k = s -1
            fork += 1
    return counter


print(F(x,T))


#A
#Tarue
#B
#x=7 , k= 1 , p = 0
#x=43 , k = 0, p = 2
#C 5 ,2

#1.2 7

#1.3 True, 0, 2