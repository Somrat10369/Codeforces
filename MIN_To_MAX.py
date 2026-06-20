import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
#mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    n = int(input())
    arr = lint()
    total = 0
    if len(set(arr)) != 1:
      for i in range(n):
        if arr[i]>min(arr):
          total+=1
    print(total)

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
