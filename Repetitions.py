import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    s = input()
    n = len(s)
    max_count=0
    current = s[0]
    count = 0

    for i in range(n):
      if s[i] == current:
        count+=1
      elif s[i] != current:
        current = s[i]
        count = 1
      max_count=max(max_count, count)
    print(max_count)

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
