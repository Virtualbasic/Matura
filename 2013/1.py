
def convert(U1):
    d = len(U1)
    num = U1
    bin  = [i for i in U1]
    f = False
    if bin[0] == "1":
       bin =  bin[1:]
       f = True
    for n in range(len(bin)):
        if bin[n] == "0":
            bin[n] = "1"
        else:
            bin[n] = "0"
    renumber = 0
    p = 0
    for i in bin[::-1]:
        if i == "1":
            renumber+=2**p
        p+=1
    if f:
        return  renumber * -1
    else:
        return  renumber

print(convert("10110"))

'''
d <- długość(U1) d > 1 
bin <- [1,d]
f <- False 
jeżeli bin[0] = "1"
    bin <- bin[1:]
    



'''