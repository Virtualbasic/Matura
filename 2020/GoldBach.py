def pierwsza(nume):
    if nume < 2:
        return False
    for i in range(2,nume //2 +1):
        if nume % i ==0:
            return  False
    return  True
allNums = []
with open("Dane_PR2/pary.txt", 'r') as fls:
    for line in fls:
        line = line.strip()
        numbers = ""
        for char in line:
            if char.isdigit():
                numbers+= char
            elif numbers:
                allNums.append(int(numbers))
                numbers=""
        if numbers:
            allNums.append(int(numbers))
onlyTR = []
for num in allNums:
    if num % 2 == 0:
        onlyTR.append(num)
firstNums = []
for first  in range(1,100):
    if pierwsza((first))==True:
        firstNums.append(first)
entry = open("data.txt" , "w")
for Goldbach in onlyTR:
    for first_num  in range(len(firstNums)):
        for seconNum in range(first_num +1 ,len(firstNums)):
            if Goldbach == firstNums[first_num] + firstNums[seconNum]:
                entry.write(str(Goldbach) + " " + str(firstNums[first_num])+ " "+ str(firstNums[seconNum]) + "\n")
                print( Goldbach , firstNums[first_num] ,firstNums[seconNum])
entry.close()