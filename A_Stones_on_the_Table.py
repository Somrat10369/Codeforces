import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(str, input().split()))

def solve():
    A = input()
    arr = list(input())
    count = 0
    if len(arr) == len(set(arr)):
      print(0)

    else:
      for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
          count+=1
      print(count)






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
