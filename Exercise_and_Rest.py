import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    n = int(input())
    print(3*n)

def main():
    solve()

if __name__ == '__main__':
    main()
