pi = [int(i.strip()) for i in open("Dane_2305/pi.txt", "r")]
ct = []
b = 0
holder = []
wskaznikzaczecia = 0
for j in range(len(pi)):
    tmp = [pi[j]]
    last_added = pi[j]
    fros = True

    for i in range(j + 1, len(pi)):
        if fros:
            if pi[i] > tmp[-1]:
                tmp.append(pi[i])
                last_added = pi[i]
            else:
                fros = False
                if pi[i] <= tmp[-1]:
                    tmp.append(pi[i])
                    last_added = pi[i]

        else:
            if pi[i] < tmp[-1] or (pi[i] == tmp[-1] and (i < len(pi) - 1) and pi[i] > pi[i+1] and pi[i] != last_added):
                tmp.append(pi[i])
                last_added = pi[i]
            else:
                break

        if len(tmp) == 6:
            ct.append(tmp)
    wskaznikzaczecia+=1

    if len(tmp) > b:
        b = len(tmp)
        holder = [tmp ,wskaznikzaczecia]

print(len(ct))
for i in ct:
    print(i)

print(f"{b , holder}")