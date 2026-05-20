import sys

min, max = map(int, sys.stdin.readline().split())

def lucky():
  found_them = 0
  for i in range(min, max+1):
    arr = set(str(i))
    if arr.issubset({'4', '7'}):
      print(i ,end=" ")
      found_them = 1
  return found_them

if not lucky():
  print(-1)


