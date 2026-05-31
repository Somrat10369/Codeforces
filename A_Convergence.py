import sys
import statistics

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    n = int(input())
    arr = lint()
    if not arr:
        print(0)
        return

    pivot = statistics.median_low(arr)
    arr = [item for item in arr if item != pivot]
    while arr and (pivot < min(arr) or pivot > max(arr) or len(arr) % 2 == 1):
        arr.append(pivot)
    print(len(arr) // 2)

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
