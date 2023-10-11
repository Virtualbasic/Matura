s = "ab"
n = len(s)
#A = [0] * (n + 1)
#B = [0] * (n + 1)
A = 0
B = 0


for i in s:
    if i == "b":
        B+=1
    elif i == "a":
        A+=1


print(A)
'''
for i in range(0,n):
    if s[i] == 'a':
        A[i] = A[i-1]+1
    else:
        A[i] = A[i-1]
print(A)
B[::-1] = 0
for j in range(n , 0 , -1):
    if s[j]== 'b':
        B[j] = B[j+1] +1
    else:
        B[j] = B[j+1]
k =1
for i in range(n+1):
    if A[i] + B[i+1] > k:
        k = A[i] + B[i+1]
print(k)
'''