with open("slowa4.txt" , "r") as s:
    sufiks = [ ]
    for i in s:
        suf = i[:-1].split()
        c = 0
        tmp = []
        for j in  suf[1]:
            tmp.append(suf[1][c:])
            c+=1
        sufiks.append(','.join(sorted(tmp)).split(",")[0])
print(sufiks)