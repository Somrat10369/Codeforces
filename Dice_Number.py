import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    arr = lint()
    Bob = int("".join(str(i) for i in sorted(arr[:3], reverse=True)))
    Alice = int("".join(str(i) for i in sorted(arr[3:], reverse=True)))
    if Bob!=Alice: print("Bob" if Bob<Alice else "Alice")
    else : print("Tie")


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
