def silnia(n):
    if n <= 1:
        return 1
    else:
        return n * silnia(n-1)

def licz_anagramy(liczba):
    liczba_jedynek = liczba.count('1')
    liczba_zer = 8 - liczba_jedynek
    return silnia(8) // (silnia(liczba_jedynek) * silnia(liczba_zer))

plik_nazwa = "anagram.txt"
liczby_z_pliku = []
max_anagramy = 0
liczby_z_max_anagramami = []


with open(plik_nazwa, 'r') as plik:
    for linia in plik:
        linia = linia.strip()
        if linia:
            if len(linia) ==8:
                liczba_anagramow = licz_anagramy(linia)
                if liczba_anagramow > max_anagramy:
                    max_anagramy = liczba_anagramow
                    liczby_z_max_anagramami = [linia]
                elif liczba_anagramow == max_anagramy:
                    liczby_z_max_anagramami.append(linia)

for liczba in liczby_z_max_anagramami:
    print(liczba)













'''

with open("anagram.txt" , "r") as ang:
    t = []
    for i in ang:
        if len(i[:-1]) == 8:
            t.append(i[:-1])

def perms(t  , l , r , res):
        if  l == r:
            res.append(t.copy())
        else:
            for i in range(l , r+1):
                t[l], t[i] = t[i] , t[l]
                perms(t, l+1 , r ,res)
                t[l], t[i] = t[i] , t[l]

g = [i for i in range(0,8)]

permutation = []

perms(g , 0, len(g)-1,g)

print(permutation)

d = {}

    holder = {

    }
    for i in ang:
        ones = 0
        zeroes = 0
        o = ''
        ze= ''
        for z in i[:-1]:

            if i[0]!= "0":
                if int(z) == 1:
                    o+=z
                    ones+=1
                else:
                    ze+=z
                    zeroes+=1

        if o+ze not in holder.keys():
            holder[o+ze] = [1 , i[:-1]]
        else:
            holder[o + ze][0] +=1
b = 0
h = []
for k, v  in holder.items():
    if v[0] > b:
        b = v[0]
        h = [k, v]
print(h)
'''











