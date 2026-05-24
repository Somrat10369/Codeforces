import sys

k , s = map(int, sys.stdin.readline().strip().split(" "))
count = 0

for i in range (k + 1):
  for j in range (k + 1):
    if i + j == s or 0 < (s - i - j) <= k :
      count += 1

print(count)
