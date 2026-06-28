import sys
import math

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
sint = lambda: map(int, input().split())

def solve():
    n = int(input())
    count=0
    for a in range(1,n+1):
      for b in range(1,n+1):
        for c in range(1,n+1):
          if math.gcd(math.lcm(a,b),math.lcm(b,c)) == math.gcd(a,c):
            count+=1
    print(count)

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
