def checkifINsquare(x,y):
    xmax = 5000
    xmin = -5000
    ymax = 5000
    ymin = -5000
    if xmin< x <xmax and ymin < y <ymax:
        return True



def checkifoNSquare(x,y):
    pass  # I will finish it someday , now I am really tired its 23.46
def checkifOUTsquare(x,y):
    xmax = 5000
    xmin = -5000
    ymax = 5000
    ymin = -5000
    if xmin> x or x >xmax or ymin > y or y  >ymax:
        return True



with open("MIN-DANE-2017/punkty.txt" , "r") as pkt:
    x = ""
    y = ""
    incount = 0
    outcount = 0
    for i in pkt:
        temptab = [z for z in i if x !='\n']
        x = "".join(temptab[:temptab.index(" ")])
        tt =temptab[temptab.index(" ")::]
        y = "".join([y for y in tt if y !=" " and y!= "\n"])
        if checkifINsquare(int(x) , int(y)):
            incount+=1
        if checkifOUTsquare(int(x) , int(y)):
            outcount +=1
    print(incount)
    print(outcount)