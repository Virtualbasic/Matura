def toin(x):
    return int(x)
def first(x):
    czynniki = []
    counter = 0

    k = 2
    while x != 1:
        while x %k ==0:
            x //=k
            czynniki.append(k)
        k+=1
    zpow = len(czynniki)
    bezpow = len(set(czynniki))

    return zpow,bezpow
    print(bezpow)
    print(czynniki)

numbers = []
with open("Dane_2205/liczby.txt", "r") as f:
    for i in f:
        numbers.append(i[:-1])



nums = list(map(toin,numbers))

największaZpowtórzeniami = 0
currentNumv1 = 0
największaBezpowtórzeń = 0
currentNumv2 = 0
for i in nums:
    temp = list(first(i))
    if temp[0] > największaZpowtórzeniami:
        największaZpowtórzeniami = temp[0]
        currentNumv1 = i
    if temp[1] > największaBezpowtórzeń:
        największaBezpowtórzeń = temp[1]
        currentNumv2 = i

print(currentNumv1)
print(currentNumv2)


#99792
#62790