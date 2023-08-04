A = [4, 2, 4, 4, 2, 6]
B = [4, 4, 2, 6, 4, 2]
K = 1
def checkTables(k ,a =[], b=[] ):
    n = len(a)

    if a[:k] == b[n-k:] and a[k:] == b[:n-k]:
        print(a[k:] ,end="first")
        print(b[:n-k], end="second")
        print("Prawda")
        return True
    else:
        print("Fałsz")
        print(a[:k] , b[k+1:])
        return False


checkTables(K, A,B)



#warunek 1
#A = [1, 2, 3, 4, 5]
#B = [3, 4, 5, 1, 2]
#K = 2
#Prawda
#warunek 2
#A = [4, 2, 4, 4, 2, 6]
#B = [4, 4, 2, 6, 4, 2]
#K = 1
#Fałsz