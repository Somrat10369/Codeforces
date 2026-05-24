import sys
n = int(sys.stdin.readline().strip())


a, b = 0, 1
for _ in range(1, n + 1):
    print(a, end = " ")
    a, b = b, a + b

