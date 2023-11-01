#a)
nums = []
def pascaltrial(nr):
    if nr == 1:
        nums.append([1])
        return [[1]]
    else:
        res_arr = pascaltrial(nr-1)
        cur_row = [1]
        prev_row = res_arr[-1]
        for i in range(len(prev_row)-1):
            cur_row.append(prev_row[i] + prev_row[i+1])
        cur_row += [1]
        res_arr.append(cur_row)
        nums.append(cur_row)
        return res_arr
tri_array = pascaltrial(30)
for i,row in enumerate(tri_array):
  for j in range(len(tri_array) - i + 1):
    print(end=" ")
  for j in row:
    print(j, end=" ")
  print("")
#b)
num = ""
count = 1
wynik5b = open("wynik5.txt" , "w")
for i in range(0 , len(nums)):
    numline = nums[i]
    for j in numline:
        num+= str(j)

    #print(( str(count) + " " + str(len(num))))
    wynik5b.write(str(count) + " " + str(len(num)) + "\n")
    num=""
    count+=1
#c)
countc = 1
def checkif(n):
    for i in n:
        if i % 5 == 0:
            return False
    return True

for i in range(0 , len(nums)):
    numline = nums[i]
    if checkif(numline):
        print(str(countc) + " " + str(numline))
    countc +=1

