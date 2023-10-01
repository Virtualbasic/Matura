def checkDivision(Number, Number2):
    a , b = Number , Number2
    if Number < 1 or Number2 < 1:
        return 0
    divesSum1 = 0
    divesSum2 = 0
    for i in range(1,Number):
        print(i)
        if Number%i ==0:
            divesSum1 += i
    for j in range(1,Number2):
        print(j)
        if Number2%j ==0:
            divesSum2 += j
    if divesSum1 == b +1 and divesSum2 == a +1:
        print(divesSum1, divesSum2)
        return True

    else:
        return  False
if checkDivision(75,48):
    print("tak")
else:
    print("nie")


