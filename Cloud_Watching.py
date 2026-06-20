import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def main():
    A, B = mint()
    print('Rain') if B>=A*3 else print('Dry')

if __name__ == '__main__':
    main()
