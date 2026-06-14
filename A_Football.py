import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input()))

def solve():
    arr = (lint())
    count = 0
    l , r = 0 , 1
    current = 1
    while r < len (arr):
      if arr[l] == arr[r]:
        current += 1
      else :
         current = 1
      l +=1
      r+=1
      count = max(count, current)
    print('YES') if count > 6 else print('NO')




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
