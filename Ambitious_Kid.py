import sys

for i in range(2):
  inpt = sys.stdin.readline().strip()
  if i == 1:
    arr = list(map(int, inpt.split()))
    print(abs(min(arr, key=abs)))
