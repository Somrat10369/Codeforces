import sys ,math

N = int(sys.stdin.readline().strip())

for i in range(2, math.floor(N**0.5)+1):
  if N % i == 0 or N <= 1:
    print("NO")
    break
else:
  print("YES")
