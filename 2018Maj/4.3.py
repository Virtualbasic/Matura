
# I was drunk


#def CheckIfIsInTable(letter, letter2):
#    LettersTab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
#                  'u', 'v', 'w', 'x', 'y', 'z']
#    letter_lower = letter.lower()
#    letter_lower2 = letter2.lower()

#    if letter_lower in LettersTab and letter_lower2 in LettersTab:
#        index1 = LettersTab.index(letter_lower)
#        index2 = LettersTab.index(letter_lower2)
#        print(abs(index1 - index2))
#        if abs(index1 - index2) < 10:
#            print(abs(index1 - index2))
#            return True

#    return False

#CheckIfIsInTable("A","H")

#with open("Dane_PR/przyklad.txt", "r") as letter:
#    for i in letter:
#        tempi = i[:-1]
#        acc = [j for j in tempi]
#        for index1 in range(0, len(acc)-1):
#            for index2 in range(index1+1,len(acc)-1):
#                if CheckIfIsInTable()
#        print(acc)


def distance_between_letters(letter1, letter2):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return abs(alphabet.index(letter1) - alphabet.index(letter2))
with open('Dane_PR/sygnaly.txt', 'r') as file:
    for line in file:
        word = line.strip()
        valid = True
        for i in range(len(word)):
            for j in range(i + 1, len(word)):
                if distance_between_letters(word[i], word[j]) > 10:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            print(word)