import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    n = int(input())
    arr= lint()
    counter = 0
    while len(set(arr)) != 1:
      n = arr.index(max(arr))
      arr[n] = (arr[n])//2
      counter+=1
    print(counter)

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
