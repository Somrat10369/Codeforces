import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def main():
    n = int(input())
    print('Yes') if 2025<=n<=2050 else print('No')

if __name__ == '__main__':
    main()
