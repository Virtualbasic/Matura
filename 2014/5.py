numbers = [int(i[:-1]) for i in open("dane/dziennik.txt"  , "r") ]
serie = []
accN = [0]
najkrotszy = numbers[0]
najdlorzszy = 0
for i in range(len(numbers)):
    if numbers[i] > najdlorzszy:
        najdlorzszy = numbers[i]
    if numbers[i] < najkrotszy:
        najkrotszy = numbers[i]
    if numbers[i] > accN[-1]:
        accN.append(numbers[i])
    elif  numbers[i] < accN[-1]:
        if len(accN) > 3:
            serie.append([accN , len(accN) , f"progres {accN[-1] - accN[0] } "] )
        accN = []
        accN.append(numbers[i])
#5.1
print(serie)
print(len(serie))
#5.2
print(najkrotszy)
print(najdlorzszy)
#5.3
najdlorzszaseria = 0
handler = []
for i in serie:
    if i[1] > najdlorzszaseria:
        najdlorzszaseria = i[1]
        handler = i
print(handler)
