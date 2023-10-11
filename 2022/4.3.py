def toin(x):
    return int(x)
def checkparameters(tab=[]):
    x , y , z = tab[0], tab[1], tab[2]
    if x==y or z==x or y==z:
        return False
    elif y %x == 0 and z%y ==0:
        return True
def kombinacje(arr, amount):
    if amount == 0:
        return [[]]
    if not arr:
        return []
    right , left = arr[0], arr[1:]
    outright = kombinacje(left,amount)
    withright = [([right]+combo) for combo in kombinacje(left, amount-1)]
    return outright + withright
def find_combinations(arr, k):
    if k > len(arr):
        return []
    return kombinacje(arr, k)

numbers = []
amount = 3

with open("Dane_2205/przyklad.txt", "r") as f:
    for i in f:
        numbers.append(i[:-1])
nums = list(map(toin,numbers))

result =find_combinations(nums,amount)

for i in result:
    if checkparameters(i):
        print(i)

#almoust done 