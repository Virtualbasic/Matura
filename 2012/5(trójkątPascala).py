#a)
nums = []
def pascaltrial(nr):
    if nr == 1:
        return [[1]]
    else:
        res_arr = pascaltrial(nr-1)
        cur_row = [1]
        prev_row = res_arr[-1]
        for i in range(len(prev_row)-1):
            cur_row.append(prev_row[i] + prev_row[i+1])
        cur_row += [1]
        res_arr.append(cur_row)
        print(cur_row)
        return res_arr
tri_array = pascaltrial(30)

for i,row in enumerate(tri_array):
  for j in range(len(tri_array) - i + 1):
    print(end=" ")
  for j in row:
    print(j, end=" ")
  print("")
print(nums)
#b)
