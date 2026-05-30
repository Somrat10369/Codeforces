import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
  A,B = mint()
  arr = sorted(lint())
  l = 0
  r = A - 1
  diff = 9999

  for r in range(A - 1, B):
    current_diff = arr[r] - arr[l]
    diff = min(current_diff , diff)
    l+=1
    r+=1

  print(diff)



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
