import sys
l1, r1, l2, r2  = map(int, sys.stdin.readline().strip().split())

l = max(l1, l2)
r = min(r1, r2)

if l <= r:
    print(f"{l} {r}")
else:
    print("-1")
