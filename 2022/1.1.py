ciag  =[5, 4, 1, 5, 6, 8]

def checkiIfPermutation(n ,ciong=[] ):
    if n !=len(ciong):
        return  -1
    expset = set(range(1, n +1))
    artset = set(ciong)
    msemelnts = expset - artset
    swaps = len(msemelnts)
    return  swaps
'''
    for i in range(len(ciong)):
        for j in range(0 , len(ciong)-i-1):
            print(i , end = "i")
            print(len(ciong)-i-1 , end = "j")
            if ciong[j]> ciong[j+1]:
                ciong[j] , ciong[j+1] = ciong[j+1], ciong[j]
    for i in ciong:
'''





print(checkiIfPermutation( 6 ,ciag ))



'''
n ciąg liczba elementów do podmiany
3 (1, 3, 1) 1
4 (1, 4, 2, 5)
5 (2, 2, 2, 2, 2)
4 (4, 2, 3, 1)
6 (5, 4, 1, 5, 6, 8)
6 (8, 4, 9, 6, 5, 7)




'''