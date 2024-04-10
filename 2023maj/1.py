

T = []
books  =[10,8,15,4,12,6,13]

for i in range(0,5):
    T.append([0]*2**i)

'''
def boo(B, i=0 , j=0):
    if T[i][j] == 0:
        T[i][j] = B
    else:
        if B < T[i][j]:
            boo(B , i+1 , 2 *j)
        elif B > T[i][j]:
            boo(B, i + 1, 2 * j +1)
rekurencyjnie 
'''

for k in books:
    i = 0
    j = 0
    while True:
        if T[i][j] == 0:
            T[i][j] = k
            break
        elif k < T[i][j]:
            i = i+1
            j = j*2
        elif k > T[i][j]:
            i = i + 1
            j = j * 2 +1

#Wypisywanie
def A(i,j):
    print(T[i][j])
    if T[i+1][2*j] !=0:
        A(i+1, 2*j)
    if T[i+1][2*j+1] !=0:
        A(i + 1, 2 * j+1)
A(0,0)
# a)
'''
9
2
12
10
14
13
15
'''
#b)
'''
10
8
4
6
15
12
13
'''

for g in T:
    print(g)