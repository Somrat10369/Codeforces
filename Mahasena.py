import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    n = mint()
    arr = lint()
    even = 0
    odd = 0
    for i in arr:
      if i % 2 == 0:
        even+=1
      else:
        odd+=1
    print("READY FOR BATTLE") if even>odd else print("NOT READY")

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
