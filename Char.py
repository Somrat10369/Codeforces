import sys
input  = sys.stdin.readline().strip()

if input.islower():
  print(input.upper())
else:
  print(input.lower())
