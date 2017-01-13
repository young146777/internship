msg = '''0x1be15dc
77676058612
03062372
676
0x9542
0x2546c9ec
02614610
0x3b3154e5a0a923ff'''

base36str = "0123456789abcdefghijklmnopqrstuvwxyz"

def hexto36(hexnum):
    decnum = int(hexnum, 16)
    return decto36(decnum)

def octto36(octnum):
    decnum = int(octnum, 8)
    return decto36(decnum)

def decto36(decnum):
    decnum = int(decnum)
    result = ""
    while decnum:
        decnum, r = divmod(decnum, 36)
        result += base36str[r].upper()
    return result[::-1]

lines = msg.splitlines()
for line in lines:
    if line[0:2] == '0x':
        print(hexto36(line))
    elif line[0:1] == '0':
        print(octto36(line))
    else:
        print(decto36(line))


