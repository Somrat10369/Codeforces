import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def main():
  A, B = mint()
  arr = lint()
  count = 0
  for i in arr:
    if i <= B : count+= 1
    else : count+= 2
  print(count)

if __name__ == '__main__':
  main()
