Dzialki = []
with open("Dane_PR2/dzialki.txt" , "r") as d:
    tmp =""
    for i in d:
        if i.isspace():
          z = tmp.replace("\n" , "")
          Dzialki.append(z)
          tmp = ""
        else:
            tmp+=i


for i in range(len(Dzialki)):
    for  j in range(i+1  , len(Dzialki) -1 ):
        if Dzialki[i][::-1] == Dzialki[j] or Dzialki[i] == Dzialki[j][::-1]:
            print([i+1 , j+1]) # indeksujemy od 0
            print(Dzialki[i])
            print(Dzialki[j])
