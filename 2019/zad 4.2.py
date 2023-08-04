def silna(num):
    suma=0
    def silnia(number):
        wynik=1
        while  number>=0:
            wynik*=number
            number-=1
            if number<=0:
                return wynik
                break
    numbers =[]
    stringnum  = str(num)
    for i in stringnum:
        numbers.append(i)
    for j in numbers:
        suma+=silnia(int(j))
    return suma

f = open("Dane_PR/przyklad.txt", "r")

for num in f:
    if int(num) == silna(int(num)):
        print(num)
print(silna(3))