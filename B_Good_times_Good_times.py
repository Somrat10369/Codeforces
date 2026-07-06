import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
#mint = lambda: map(int, input().split())
#lint = lambda: list(map(int, input().split()))
#sint = lambda: map(int, input().split())

good = []
for i in range(2,1000):
   if len(set(str(i)))<=2:
     good.append(i)


def solve():
  a = int(input())
  found = False
  for b in good:
     c = b*a
     if len(set(str(c)))<=2:
       print(b)
       found = True
       break

  if not found:
    for b in range(max(good)+1,1000000):
      if len(set(str(b))) <= 2:
        good.append(b)
        c = b*a
        if len(set(str(c)))<=2:
          print(b)
          break


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
