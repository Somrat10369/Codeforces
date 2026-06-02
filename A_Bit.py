import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
  n = int(input())
  initial = 0
  for i in range(n):
    s = input()
    if s == "++X" or s == "X++": initial +=1
    elif s == "--X" or s == "X--": initial -=1
  print(initial)

def main():
    sys.setrecursionlimit(200000)

    t = 1
    #try:
        #t = int(input())
    #except ValueError:
        #pass

    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
