
with open('Dane_2203/szachy.txt', 'r') as file:
    linie = file.readlines()


liczba_linii = len(linie)
liczba_znakow = len(linie[0].strip())

tablica = [[' ' for _ in range(liczba_znakow)] for _ in range(liczba_linii)]


for numer_linii, linia in enumerate(linie):
    for numer_znaku, znak in enumerate(linia.rstrip('\n')):
        tablica[numer_linii][numer_znaku] = znak


for linia in tablica:
    print(''.join(linia))

#test