import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    n = int(input())
    hashmap = Counter(input())
    if hashmap["D"] > hashmap["A"]: print("Danik")
    elif hashmap["D"] < hashmap["A"]: print("Anton")
    else: print("Friendship")

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
