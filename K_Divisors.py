import sys

N = int(sys.stdin.readline().strip())

for i in range(N+1):
  if i != 0 and  N%i == 0:
    print(i)
