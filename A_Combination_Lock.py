import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    n = int(input())
    current = list(input())
    target = list(input())
    total = 0

    for i in range(n):
      diff1 = abs(int(target[i]) - int(current[i]))
      diff2 = abs(int(target[i]) - int(current[i]) - 10)
      diff3 = abs(int(target[i]) - int(current[i]) + 10)
      diff = min(diff1, diff2,diff3)
      total += diff

    print(total)


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
