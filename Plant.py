import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
sint = lambda: map(int, input().split())

def solve():
    n = int(input())
    arr = lint()
    if n == 2:
      print(min(arr))
    else:
      mx = -1
      for i in range(1,n):
        cmx = min(arr[i-1], arr[i])
        mx = max(cmx,mx)
      print(mx)

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
