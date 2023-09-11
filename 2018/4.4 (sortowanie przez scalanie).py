
c1 = []
c2 = []

numc1 = []
numc2 = []

c3 = []
def mapforint(c):
    return int(c)
def mergeSort(arr1, arr2):
    def merge(left , right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i +=1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    if len(arr2) <=1 and len(arr1) <=1:
        return merge(arr1,arr2)
    mid1 = len(arr1)//2
    mid2 = len(arr2)//2
    left1 , right1 = arr1[:mid1], arr1[mid1:]
    left2, right2 = arr2[:mid2], arr2[mid2:]
    sorted_left = mergeSort(left1,left2)
    sorted_right = mergeSort(right1,right2)
    return  merge(sorted_left,sorted_right)
with open("dane/NM_DANE_PR/przyklad1.txt" , "r") as cn1:
    for i in cn1:
        c1.append(i[:-1].split())

with open("dane/NM_DANE_PR/przyklad2.txt" , "r") as cn2:
    for i in cn2:
        c2.append(i[:-1].split())

for j in c1:
    checkhrs = [i for i in j]
    intchker = map(mapforint ,checkhrs)
    listchkr = list(intchker)
    numc1.append(listchkr)

for j in c2:
    checkhrs = [i for i in j]
    intchker = map(mapforint ,checkhrs)
    listchkr = list(intchker)
    numc2.append(listchkr)

for i in range(0,len(numc2)):
    print(mergeSort(numc1[i], numc2[i]))


#for i in range(0,len(numc1)):
#    c3temp = []
#    for j in range(0,9):
#        print(numc1[i][j])
#        print(numc2[i][j])
#        if numc1[i][j] > numc2[i][j]:
#            print(c3temp)
#            c3temp.append(numc2[i][j])
#        elif numc1[i][j] < numc2[i][j]:
#            c3temp.append(numc1[i][j])
#        elif numc1[i][j] == numc2[i][j]:
#            c3temp.append(numc1[i][j])
#    c3.append(c3temp)
#    c3temp.clear()
#print(c3)
#print(numc2)
#print(numc1)