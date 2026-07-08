import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
#mint = lambda: map(int, input().split())
lint = lambda: list(map(int, sys.stdin.readline().rstrip("\r\n").split()))
#sint = lambda: map(int, input().split())

def solve():
    n = int(input())
    arr = lint()
    ttl = 0
    cmx = arr[0]
    for i in range(1,n):
      if arr[i] < cmx:
        ttl +=(cmx-arr[i])
      else:
        cmx = arr[i]
    print(ttl)

def main():
    sys.setrecursionlimit(200000)
    t = 1
    try:
        t = int(input())
    except ValueError:
        pass

    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
