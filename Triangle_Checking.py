import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def main():
    arr = lint()
    ok = True
    for i in range(len(arr)):
      if sum(arr)-arr[i]<=arr[i]:
        ok = False
        break
    print('Yes') if ok else print('No')

if __name__ == '__main__':
    main()
