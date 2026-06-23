import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def main():
    n = int(input())
    print(1) if n%2 == 0 else print(2)

if __name__ == '__main__':
    main()
