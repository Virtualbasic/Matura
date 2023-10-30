n = 31
def s(n):
    result = 0
    for i in range(1,n+1):
        for j in str(i):
            result+=int(j)
        if result + i  == n:
            k = i
            print(k)
            print(result)
            return True
        else:
            result = 0
if s(n):
    print("Tak")
else:
    print("Nie")


#28 23 5
# Nie