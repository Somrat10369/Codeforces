import sys
input  = int(sys.stdin.readline().strip())

for i in range (12):
  result = input*(i+1)
  print(f"{input} * {i+1} = {result}")
