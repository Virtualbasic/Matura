def checkamountOFchars(s):
    sr = {}
    for i in s:
        if i in sr.keys():
            sr[i]+=1
        else:
            sr[i] = 1
    return  len(sr)

print(checkamountOFchars("aaaaaaaaaaaaaaaaaaaaaf"))