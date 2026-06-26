import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
sint = lambda: map(int, input().split())

def solve():
    n, k = mint()
    arr = sint()
    state = False
    wasted = float('inf')
    for i in arr:
      if i>=k:
        state = True
        curr = i%k
        wasted = min(curr, wasted)
    if state: print(wasted)
    else: print(-1)

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
