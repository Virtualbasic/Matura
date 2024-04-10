instrukcje = []
with open("DANE_2105/przyklad.txt" , "r") as instr:
    for i in instr:
        instrukcje.append([i[:-3] ,i[-2:-1]] )
character = []
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
instructions = ["DOPISZ", "ZMIEN", "USUN" , "PRZESUN"]
dict = {"A":1}
print(instrukcje)
for i in range(0 , len(instrukcje)-1):
    if instrukcje[i][0] ==instructions[0]:
        if instrukcje[i][1] in dict.keys():
            dict[instrukcje[i][1]] += 1
        else:
            dict[instrukcje[i][1]] = 1
        character.append(instrukcje[i][1])
    elif instrukcje[i][0] ==instructions[1]:
        character[-1:] = instrukcje[i][1]
    elif instrukcje[i][0] == instructions[2]:
        character =character[:-1]
    elif instrukcje[i][0] == instructions[3]:
        if instrukcje[i][1] in character:
            inx =alpha.index(instrukcje[i][1])-1
            for j in character:
                if j == instrukcje[i][1]:
                    instrukcje[i][1] = alpha[inx+1]
                    break
                if j == "Z":
                    instrukcje[i][1] = "A"

print(character)
ch = ""
for i in character:
    ch +=i
print(ch)
print(dict)