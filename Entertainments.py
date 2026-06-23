import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def main():
    n = int(input())
    print(n*200 if n*200<1000 else 1000)

if __name__ == '__main__':
    main()
