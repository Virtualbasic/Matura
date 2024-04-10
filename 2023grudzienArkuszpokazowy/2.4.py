numbers = [i[:-1].split(" ")  for i in open("Dane_2212/pary.txt" ,"r")]
warunek = []
for n in numbers:
    a = int(n[0])
    b = int(n[1])
    while b>a:
        b//=2
        if b == a:
            warunek.append(n)
            break
print(warunek)