w = open("Data/4.1.txt" , "w")
def checking(number):
    num = int(number)
    result = 1
    pt =0
    if num == 1:
        return True
    while num > result:
        result *=3
        pt+=1
    if num == result:
        return True

with open("Dane_PR/przyklad.txt" , "r") as f:
    for num in f :
        if int(num)%3==0:
            if checking(int(num)):
                w.write(num )
        elif int(num)==1:
            w.write(num)
