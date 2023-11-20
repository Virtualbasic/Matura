def pierw(num):
    if num < 2:
        return  False
    else:
        for i in range(2,int(num**0.5) +1):
            if  num % i == 0:
                return False
    return  True
with open("MIN-DANE-2017/punkty.txt" , "r") as pkt:
    x = ""
    y = ""
    for i in pkt:
        temptab = [z for z in i if x !='\n']
        x = "".join(temptab[:temptab.index(" ")])
        tt =temptab[temptab.index(" ")::]
        y = "".join([y for y in tt if y !=" " and y!= "\n"])
        if pierw(int(x)) and pierw(int(y)):
            print(f"x:{x} y:{y}  są liczbami pierwszymi")