import sys
from math import log as ln
A, B, C, D  = map(int, sys.stdin.readline().strip().split())

print("YES") if B*ln(A) > D*ln(C) else print("NO")
