import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    n = int(input())
    arr = lint()
    if not arr:
        print(0)
        return

    count = 0
    i = 0
    while i < len(arr) - 1:
        if arr[i] % 2 == arr[i + 1] % 2:
            arr[i + 1] = arr[i] * arr[i + 1]
            del arr[i]
            count += 1
        else:
            i += 1

    print(count)

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
