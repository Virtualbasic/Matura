def dectobin(dec):
    binnum = ""

    if dec ==0:
        return "0"
    while dec>0:
        tempbin = dec%2
        binnum = str(tempbin) + binnum
        dec = dec//2

    return binnum

print(dectobin(45))

print(int("2D" , 16))
# (1111011 XOR 0101101)  => 1010110
# (1010110 XOR 0101101) => 1111011
#  0101101
#
#