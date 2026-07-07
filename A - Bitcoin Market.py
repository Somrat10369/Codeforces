import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
#mint = lambda: map(int, input().split())
#lint = lambda: list(map(int, input().split()))
#sint = lambda: map(int, input().split())

def main():
    n = int(input())
    print('YES') if n<=4 else print('NO')

if __name__ == '__main__':
    main()
