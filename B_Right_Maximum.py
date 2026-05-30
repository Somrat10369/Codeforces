import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
lint = lambda: list(map(int, input().split()))

def solve():
    n = int(input())
    arr = lint()

    count = 0
    current_max = -1

    for i in range(n - 1, -1, -1):
        if arr[i] >= current_max:
            current_max = arr[i]
            count += 1

    print(count)

def main():
    t = 1
    try:
        t = int(input())
    except ValueError:
        pass

    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
