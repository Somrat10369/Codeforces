import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def main():
    n = int(input())
    if n>15:print(-1)
    else: print(15-n)

if __name__ == '__main__':
    main()
