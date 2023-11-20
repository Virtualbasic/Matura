'''
def reg(w):
    if len(w) == 1:
        return 1
    elif len(w) % 2 ==  1:
        w1 = w[:len(w)//2]
        Z = w[len(w)//2]
        w2 =   w[len(w)//2 +1:]
        if w1 == w2 and (Z == 'A' or Z == 'B'):
            return reg(w) +1
    elif len(w) % 2 ==  0:
        w1 = w[:len(w) // 2]
        w2 = w[len(w) // 2:]
        if w1 == w2:
            return  reg(w) + 1
    return  0
'''
def palin(word):
    return word[::-1]
def reg(word):
    if len(word)==1:
        return  1
    elif len(word) % 2 == 1:
        md_index = len(word)//2
        w1 = word[:md_index]
        Z = word[md_index]
        w2 = word[md_index+1:]
        if palin(w1):
            return reg(w1) +1
        else:
            return  0
    else:
        md_index = len(word) // 2
        w1 = word[:md_index]
        w2 = word[md_index:]
        if palin(w1):
            return  reg(w1) +1
        else:
            return  0
testcase = "AAAAAAAA"
print(reg(testcase))
# A 1
# BABBAB  3
# BABBBB  3
# BAAAAB 3
# B  1
#BBB 2
# AAAAAAAA  4
