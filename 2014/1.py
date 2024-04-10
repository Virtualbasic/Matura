def potega(n,a):
    p = 2
    result = n
    while p<=a:
        result*=n
        p+=1
    return  result


def armstr(n):
    def TFisthat(n):
        return [int(i) for i in str(n)[::-1]]
    nums = TFisthat(n)
    res = 0
    for i in nums:
        res += potega(int(i),3)
    return True if res == n else False



print(armstr(32))


#1
'''
6 NIE 

407  TAK

2278 NIE 
'''