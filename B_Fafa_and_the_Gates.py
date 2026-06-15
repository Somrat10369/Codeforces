import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
#mint = lambda: map(int, input().split())
lint = lambda: list(map(str, input()))

def solve():
    n = int(input())
    arr = input()
    x,y = 0,0
    coin = 0

    for i in range(n-1):
      if arr[i] == "R": x+=1
      else: y+=1
      if x==y and arr[i] == arr[i+1]:
        coin+=1
    print(coin)

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
