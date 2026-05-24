import sys

n = int(sys.stdin.readline().strip())

def dec_to_bin(dc):
    if dc == 0: return "0"
    elif dc == 1: return "1"
    else: return dec_to_bin(dc // 2) + str(dc % 2)

def bin_to_dec(bn):
    bn = bn.replace("0", "")
    decimal = 0
    for digit in bn:
        decimal = decimal * 2 + int(digit)
    return decimal

for i in range (n):
  inpt = int(sys.stdin.readline().strip())
  print(bin_to_dec(dec_to_bin(inpt)))

