import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
sint = lambda: map(int, input().split())

def main():
    n = int(input())
    arr = sint()

    print((n*(n+1)//2)-sum(arr))

if __name__ == '__main__':
    main()
