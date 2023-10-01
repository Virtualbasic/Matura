A = [4,6,3,5,2,1]

def przestaw(A=[]):
    n = len(A)
    key = A[1]
    w = 1
    for k in range(2,n):
        if A[k]< key:
            A[w] , A[k] = A[k], A[w]
            w = w +1
    return A
newA = przestaw(A)
print(newA)