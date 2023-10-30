def deszyfr(wor, ke):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ascii = [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
    i = 0
    password = ""
    word = wor
    key = ke
    j = 0
    while len(key) != len(word):
        key = key + key[j]
        j += 1
    while i < len(word):
        wordletter = word[i]
        keyletter = key[i]
        wordalpha = alphabet.index(wordletter)
        keyalpha = alphabet.index(keyletter)
        if ascii[wordalpha] + keyalpha+1 > 90:
            res = ((ascii[wordalpha] + keyalpha) - 25)
            password += alphabet[ascii.index(res)]
            i += 1
        else:
            password += alphabet[ascii.index(ascii[wordalpha]) + keyalpha+1]
            print(ascii.index(ascii[wordalpha] + keyalpha))
            i += 1
    return password
keys = []
words = []
with open("Dane/tj.txt", "r") as wordd:
    for w in wordd:
        words.append(w[:-1])
with open("Dane/klucze1.txt", "r") as keyy:
     for k in keyy:
         keys.append(k[:-1])
a = open("wynik4a.txt", "w" , encoding="utf8")
print(words)
print(keys)

for i in range(0 , len(words)):
    print(words[i])
    print(keys[i])
    print(deszyfr(words[i], keys[i]))
    a.write("słowo:" + words[i] +", klucz: " + keys[i] +" = " + deszyfr(words[i], keys[i]) +"\n" )