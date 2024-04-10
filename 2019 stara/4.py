Dzialki = []
with open("Dane_PR2/dzialki.txt" , "r") as d:
    tmp =""
    for i in d:
        if i.isspace():
          z = tmp.replace("\n" , "")
          c = 0
          for t in z:
              if t == "*":
                  c+=1
          Dzialki.append([z , c /(900)])
          tmp = ""
        else:
            tmp+=i

b = 0.7

for i in Dzialki:
    if i[1]>= b:
        print(i)
