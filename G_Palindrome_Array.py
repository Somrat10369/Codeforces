import sys

left , right  = 0 ,int(sys.stdin.readline())
main = list(map(int, sys.stdin.readline().strip().split(" ")))

output = 1

for i in range (left , right):
  j = (right - 1) - i
  if main[i] != main[j]:
    output = 0
    break

print("YES") if output == 1 else print("NO")
