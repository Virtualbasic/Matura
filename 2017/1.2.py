A = [4, 34, 16, 8, 6, 22, 14, 12, 2, 7 ]
def oblicz(p , A=[]):
    pola = []
    for i in range(0 ,len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] != A[j] and A[i] * A[j]%p != 0:
                pola.append(A[i] * A[j])
    biggest = 0
    for big in pola:
        if big > biggest:
            biggest = big
    print(pola)
    return biggest
print(oblicz(2 ,A))




'''
15, 12, 10, 6, 5, 1 =72
6, 28, 7, 12, 10, 14, 5, 9, 4, 8, 18  = 216
4, 34, 16, 8, 6, 22, 14, 12, 2, 7 = 0
'''