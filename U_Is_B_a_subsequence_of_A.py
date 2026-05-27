import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
  m, n = mint()
  A = lint()
  B = lint()

  i, j = 0,0
  while i < m and j < n:
    if A[i] == B[j]:
      j+=1
    i+=1

  print ("YES") if j == n else print("NO")

def main():
    sys.setrecursionlimit(200000)

    t = 1
   # try:
   #     t = int(input())
   # except ValueError:
   #     pass

    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
