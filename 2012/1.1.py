def F(i, a):
    n = 2012
    if i == n:
        return n
    else:
        j = F(i + 1,a)
        if a[i] < a[j-1]:
            return i
        else:
            return j
a = [5, 1, 8, 9, 7, 2, 3, 11, 20, 15]
print(F(512, a))

#a
#9 10
# 7 7
# 5 5 should be fucking 6
#b
# najmniejszą liczbą w tej tablicy spośród elementów o indeksach od i do n.
#c
#