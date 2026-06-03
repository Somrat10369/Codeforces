import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    n = (input())
    ln = list(n)
    upper = list(n.upper())
    lower = list(n.lower())
    print (n.upper()) if sum((Counter(ln) & Counter(upper)).values()) > sum((Counter(ln) & Counter(lower)).values()) else print (n.lower())


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
