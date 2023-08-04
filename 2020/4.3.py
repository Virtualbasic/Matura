characters ={}
with open("Dane_PR2/przyklad.txt", 'r') as fls:
    for line in fls:
        line = line.strip()
        word = ""
        num = ""
        for char in line:
            if char.isdigit():
                num += char
            elif char.islower():
                word += char
        if num and word:
            characters[int(num)] = word


print(characters)

keyss = []
itemss = []

for key in characters.keys():
    keyss.append(key)
    itemss.append((characters[key]))
print(keyss)
min_key = keyss[0]
min_item = itemss[0]
for keyv1 in keyss:
    for val in itemss:
        if keyv1<min_key and val < min_item:
            min_item = val
            min_key = keyv1


with open("dane4.3.txt" , "w") as fls:
    fls.write(str(min_key) + " "  + str(min_item))
print(itemss)
print(min_key)
print(min_item)
