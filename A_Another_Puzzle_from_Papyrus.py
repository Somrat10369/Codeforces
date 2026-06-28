import sys

#input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, sys.stdin.readline().rstrip("\r\n").split())
lint = lambda: list(map(int, sys.stdin.readline().rstrip("\r\n").split()))
#sint = lambda: map(int, input().split())

def solve():
    n,c = mint()
    a = lint()
    b = lint()

    cost_nt = 0
    cost_t = 0

    flag_nt = True
    for i in range(n):
      if a[i]<b[i]:
        flag_nt = False
      cost_nt += (a[i] - b[i])

    a.sort()
    b.sort()

    flag_t = True
    for i in range(n):
      if a[i]<b[i]:
        flag_t = False
        break
      cost_t += (a[i] - b[i])

    if not flag_nt and not flag_t : print(-1)
    elif not flag_nt:print(cost_t+c)
    elif not flag_t:print(cost_nt)
    else: print(min(cost_nt,cost_t+c))


def main():
    sys.setrecursionlimit(200000)

    t = 1
    try:
        t = int(input())
    except ValueError:
        pass

    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
