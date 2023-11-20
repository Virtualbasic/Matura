def sitko(n):
    counterforczyjest = 0
    k= 75
    czyjest = [False] * (n+1)
    print(czyjest)
    j = 1
    while j*j < n:
        j = j +1
    for i in range(2,j):
        kw = i*i
        poz = kw
        while poz <= n:
            if i ==9:
                counterforczyjest +=1
            czyjest[poz] = True

            poz = poz + kw
    print(czyjest)
    print(counterforczyjest)
    return j , czyjest[k]

print(sitko(100))

'''
1)
n  |  k  |  j  |  czy_jest[k]
10    9     4    false 
100   10   10    flase 
100   75   10    true
2)

i |     liczba wykonań wiersza 
3    11 
5     4 
9     1

3)
25 + 11 + 4 + 1 = 41 

100
100 (cos tam)


'''
