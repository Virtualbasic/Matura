def some(n, A):
    max = 1
    nr =  1
    pp = 0
    for i in range(n):
        k = 0
        for j in range(i+1 , n):
            pp += 1
            if A[i] == A[j]:
                k +=1
        if k > max:
            max = k
            nr =  i
    print(pp)
    return A[nr]


print(some( 1000   , [2]*1000))

# 1
# 2
# 3

