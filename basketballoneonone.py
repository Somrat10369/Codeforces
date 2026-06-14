import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(str, input()))

def solve():
    n = (lint())
    A = 0
    B = 0
    for i in range(0, len(n), 2):
      if n[i] == "A":
        A+=int(n[i+1])
      else:
        B+=int(n[i+1])
    print("A") if A>B else print("B")


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
