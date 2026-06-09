import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    n = int(input())
    vec = [0,0,0]
    for _ in range(n):
      arr = lint()
      vec = [x + y for x, y in zip(arr, vec)]

    print('YES') if set(vec) == {0} else print('NO')

def main():
    sys.setrecursionlimit(200000)

    t = 1
    #try:
        #t = int(input())
    #except ValueError:
        #pass

    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
