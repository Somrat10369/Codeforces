import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def main():
    A, B = mint()
    print(A-B) if A>B else print(0)

if __name__ == '__main__':
    main()
