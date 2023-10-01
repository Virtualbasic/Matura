# a > 1 b

def checkDivision(Number):
    a  = Number
    if a< 1 :
        return 0
    divesSum1 = 0

    for i in range(1,a):
        if a%i ==0:
            divesSum1 += i
    return divesSum1-1

a = 50


print(checkDivision(a))