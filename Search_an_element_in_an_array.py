import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: set(map(int, input().split()))

def solve():
    N, X = mint()
    A = lint()
    print('YES') if X in A else print('NO')

if __name__ == '__main__':
    solve()

