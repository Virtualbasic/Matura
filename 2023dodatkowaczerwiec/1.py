def iloczyn(x,y):
    addingCounter = 0
    if y == 1:
        return  x
    else:
        k = y //2
        z = iloczyn(x,k)
        if  y % 2 ==0:
            '''
            print(x , end= "x \n")
            print(y , end = "y \n")
            print(k, end=" k \n")
            print(z, end=" z  \n ")
            print(z+z)
            print("---------------")
            addingCounter+=1
             '''
            print("1")
            return  z+z
        else:
            '''
            print(x, end="x \n")
            print(y, end="y \n")
            print(k, end=" k \n")
            print(z , end= " z  \n ")
            print(x + z + z)
            print("---------------")
            '''
            print("2")
            return  x + z + z
iloczyn(112,112)
# 1.1
'''
10x 
2y 
1 k 
10 z  
 20
---------------
10x 
5y 
2 k 
20 z  
 50
---------------
10x 
11y 
5 k 
50 z  
 110
---------------
10x 
22y 
11 k 
110 z  
 220
---------------
10x 
45y 
22 k 
220 z  
 450
---------------
                to 1 ^ 
'''


# x   y
'''
  9   11    5 
  8   32    5 
  2   47    9
  112 112   8 
'''