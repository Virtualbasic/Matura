counter = 0
with open("Dane_2205/liczby.txt", "r") as  f:
    for i in f:
        num = i[:-1]
        rewnum = num[::-1]
        if int(num[0]) == int(rewnum[0]):
            print(num)
            counter+=1

print(counter)