import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def main():
    n = int(input())
    total = 0
    mx = 0
    for _ in range(n):
      A,B = mint()
      total = total - A + B
      mx = max(mx, total)
    print(mx)

if __name__ == '__main__':
    main()
