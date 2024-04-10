def iloczyn(x,y):

    if y==1:
        return x
    else:
        k= y//2

        z = iloczyn(x,k)
       # print(f" k= {k} , z ={z} , x = {x} , y = {y} ")
        if y % 2 == 0:
            print(1, end="dla1 ")
            return z+z
        else:

            print(1)
            return x +z +z

x,y =2,47
print(iloczyn(x,y))

'''
1
 k= 1 , z =10 , x = 10 , y = 2 
 k= 2 , z =20 , x = 10 , y = 5 
 k= 5 , z =50 , x = 10 , y = 11 
 k= 11 , z =110 , x = 10 , y = 22 
 k= 22 , z =220 , x = 10 , y = 45 
1.2
x,y = 8,32   5 
x,y = 2,47   9
x,y =112,112 8
'''