import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    arr = lint()
    found = False
    for i in arr:
      if sum(arr)-i<i:
        print('YES')
        found = True
    if not found:
      print('NO')


def main():
    sys.setrecursionlimit(200000)

    t = 1
    try:
        t = int(input())
    except ValueError:
        pass

    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
