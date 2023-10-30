
def s(n):
    result = 0
    for i in range(1,n+1):
        for j in str(i):
            result+=int(j)
        if result + i  == n:
            k = i
            print(k)
            print(result)
            return  result
        else:
            result = 0
results = []
for i in range(1000,9999+1):
    if s(i)!= 0 and s(i) != None:
        print("Tak")
        results.append(s(i))
    else:
        print("Nie")
print(results)
bigest =  0
for i in results:
    if i > bigest:
        bigest = i
print(bigest)
#suma cyfr w 4 cyfrowej liczbie nie może być większa od 36 dla największej liczby 9999 jest to 36 dlatego s(k)<=36 największe s(k) równe jest 35 co potwierdza ten warunek