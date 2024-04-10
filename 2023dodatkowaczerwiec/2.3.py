def czymniejszy(n,s,k1,k2):
    i = k1
    j = k2
    while i <= n and j <= n:
        if s[i-1] == s[j-1]:
            i += 1
            j += 1
        else:
            if s[i] < s[j]:
                return True
            else:
                return  False
    if j <= n:
        return  True
    else:
        return  False

s = "mascarpone"
n = len(s)

T = [i for i in range(1, n+1)]
for j in range(1 , n-1):
    for g in range(1,n -j):
        if not czymniejszy(n,s,j,j+1):
            x = T[j+1]
            T[j+1] = T[j]
            T[j] = x
print(T)

