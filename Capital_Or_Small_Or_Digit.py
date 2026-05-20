import sys
input  = sys.stdin.readline().strip()

if input.isnumeric():
  print("IS DIGIT")
elif input.islower():
  print("ALPHA")
  print("IS SMALL")
else:
  print("ALPHA")
  print("IS CAPITAL")
