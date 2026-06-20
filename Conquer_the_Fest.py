import sys

#input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
#lint = lambda: list(map(int, input().split()))

def main():
    A, B = mint()
    print('YES') if A>=10*B else print('NO')

if __name__ == '__main__':
    main()
