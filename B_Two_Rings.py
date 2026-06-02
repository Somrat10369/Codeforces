import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    A,B,C, X, Y, R = mint()
    delta = ((A-X)**2 + (B-Y)**2)
    print('Yes') if abs(C-R)**2 <= delta <= (C+R)**2  else print('No')


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
