import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    n = 5
    r = 0
    c = 0
    for i in range(n):
      arr = lint()
      if sum(arr)==1:
        c = i + 1
        r = arr.index(1) + 1
        break
    print(abs(3-r) + abs(3-c))







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
