import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    o, t = mint()
    if o % 2 == 1:
        print("NO")
    elif t % 2 == 0:
        print("YES")
    else:  
        print("YES" if o >= 2 else "NO")

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
