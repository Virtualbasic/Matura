def d(x, tab):
    n = len(tab) - 1
    n = n + 1
    tab.append(x)
    s = n
    while s > 0 and tab[s] > tab[(s - 1) // 2]:
        pom = tab[s]
        tab[s] = tab[(s - 1) // 2]
        tab[(s - 1) // 2] = pom
        s = (s - 1) // 2
    return tab

tab = [327, 6, 13, 4, -3, -2, -3]
print(d(30, tab))

#[36, 15, 17, 3, -5]
#[327, 30, 13, 6, -3, -2, -3, 4]