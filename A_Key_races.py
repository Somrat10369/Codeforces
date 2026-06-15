import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    S, Vo , Vt, To, Tt = mint()
    if 2*To+S*Vo < 2*Tt+S*Vt:
      print("First")
    elif 2*To+S*Vo > 2*Tt+S*Vt:
      print("Second")
    else:
      print("Friendship")

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
