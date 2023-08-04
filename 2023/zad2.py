def Tura(k, B, A):
    s = len(B) - 1
    if k > len(A) or A[k - 1] > s:
        return

    for i in range(s, A[k - 1] - 1, -1):
        print(i)
        if B[i - A[k - 1]] == 1 and B[i] == 0:
            B[i] = 1


def play_game(s, n, A):
    max_value_A = max(A)
    B = [0] * (max(s, max_value_A) + 1)
    B[0] = 1

    for k in range(1, n + 1):
        Tura(k, B, A)

    return B

s = 500
A = []
for i in range(5,105,5):
    A.append(i)
print(A)
n = len(A)
wynik = play_game(s, n, A)

AmountOfpawns = 0
for i in wynik:
    if i == 1:
        AmountOfpawns+=1
if wynik[s] == 1:
    print("Gra zakończyła się sukcesem. Na polu B[s] stoi pionek.")
else:
    print("Gra nie zakończyła się sukcesem. Na polu B[s] nie stoi pionek.")
print(AmountOfpawns)
#[1, 2, 5, 10]  nie
#[13, 5, 5, 2, 7]  tak
#[7, 6, 5, 4, 3, 2, 1] tak

#2.2
# 101