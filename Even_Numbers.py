import sys
input  = int(sys.stdin.readline().strip())

for i in range (input+1):
  if i%2 == 0 and i!= 0:
    print(i)
if input < 2:
  print (-1)
