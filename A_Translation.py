import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def main():
    m = (input())
    n = (input())
    l,r = 0 , len(n)-1
    ok = True

    if len(m) != len (n):
      ok = False
    else:
      for i in (n):
        if m[l] == n[r]:
          try:
            l+=1
            r-=1
          except IndexError:
            pass
        else:
          ok = False
          break

    print('YES') if ok else print('NO')

if __name__ == '__main__':
    main()
