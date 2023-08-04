def longest_common_c(string):
    n_c = ""
    a_c = ""
    for z in string:
        if a_c == "":
            a_c = z
        elif z  == a_c[-1]:
            a_c += z
        else:
            if len(a_c)  > len(n_c):
                n_c = a_c
            a_c = z
    if len(a_c) > len(n_c):
        n_c = a_c
    return n_c

words = []
with open("Dane_PR2/pary.txt", 'r') as fls:
    for line in fls:
        line = line.strip()
        word = ""
        for char in line:
            if char.islower():
                word += char
            elif word:
                words.append(word)
                word = ""
        if word:
            words.append((word))
entry = open("data2.txt" , "w")

commons = []

for strn in words:
    some = longest_common_c(strn)
    if len(some) < 2:
        pass
    else:
        pom = len(some)
        entry.write(longest_common_c(strn)  + " " +  str(pom) + "\n" )
        commons.append(longest_common_c(strn))

print(commons)