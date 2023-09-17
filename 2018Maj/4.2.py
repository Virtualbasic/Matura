forsyg = []
with open("Dane_PR/przyklad.txt" , "r") as f:
    for  i in f:
        forsyg.append(i[:-1])


def onlyOneLetter(word):
    dict = {key: 0 for key in word}
    countappears = 0
    for i in word:
        if i in dict:
            dict[i] += 1
    for val in dict.values():
        if val ==1:
            countappears +=1
    return len(dict)
def countA(word):
    counter = 0
    for i in word:
        if i == "A":
            counter+=1
    return counter
dictforwords = {}
for i in forsyg:
    dictforwords[i] = onlyOneLetter(i)
word = ""
wordlen = 0
for key , val in dictforwords.items():
    if len(key)>len(word) and val > wordlen:
        word = key
        wordlen = val
print(dictforwords)
print(word + " " + str(wordlen))


