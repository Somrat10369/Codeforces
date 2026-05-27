import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():

  n = int(input())
  main_diagonal_sum=0
  secondary_diagonal_sum=0

  arr = []
  for i in range(n):
     arr.append(lint())

  for i in range(n):
     main_diagonal_sum+=arr[i][i]
     secondary_diagonal_sum+=arr[i][n - 1 - i]

  print(abs(secondary_diagonal_sum - main_diagonal_sum))

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
