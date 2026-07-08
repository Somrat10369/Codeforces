import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
sint = lambda: map(int, input().split())

def main():
    a, b, c = mint()
    print(3*a + b)

if __name__ == '__main__':
    main()
