def reg(w,n):
    if n == 1 :
        return 1
    elif n % 2 == 0:
            m = n//2
    else:
        m = (n-1) //2
    for i in range(1, m+1):
            if w[i-1] != w[n-i]:
                return  0
    x = w[:m]
    return  1 + reg(x, m)

testcase =  "BBB"
# n = len(testcase)
print(reg(testcase, 3))
