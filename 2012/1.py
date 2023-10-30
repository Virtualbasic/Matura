def bin(x):
    if x == 0:
        return '0'
    binnum = ""
    negnum = False
    if x <0:
        negnum = True
        decnum = abs(x)

    while decnum  > 0:
        rest = decnum  % 2
        binnum = str(rest) + binnum
        decnum = decnum  // 2

    if negnum:
        while len(binnum)<8:
            binnum=  '0' + binnum
        binnum = ''.join('1'if bit == '0' else '0' for bit in binnum)
        binnum  = '1'  + binnum
    return binnum

print(bin(-37))