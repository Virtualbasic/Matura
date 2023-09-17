n= 730
p =1
g = n

while p<g:
    s = (p+g)//2
    if s*s*s < n:
        p = s+1
        print(p)
    else:
        g = s

#n = 28 p = 4 or 3.6875
#n = 64 p = 4 or 3.96875 4.9990234375
#n = 80 p = 5 or 4.46875


#1.2 lowest 730 , 1000