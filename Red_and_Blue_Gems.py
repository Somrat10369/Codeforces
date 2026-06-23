import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def main():
    A, B,C, D  = mint()
    print(A*C) if A*C>B*D else print(B*D)

if __name__ == '__main__':
    main()
