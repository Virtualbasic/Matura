def checkifsame(x , y):
    for i in x:
        if i not in y:
            return  False
    for j in y:
        if j not in x:
            return  False
    return True
with open("MIN-DANE-2017/punkty.txt" , "r") as pkt:
    x = ""
    y = ""
    for i in pkt:
        temptab = [z for z in i if x !='\n']
        x = "".join(temptab[:temptab.index(" ")])
        tt =temptab[temptab.index(" ")::]
        y = "".join([y for y in tt if y !=" " and y!= "\n"])
        if checkifsame(x,y):
           print(f"x:{x}  y:{y} są cyfro podobne")