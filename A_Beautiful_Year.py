import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def main():
    n = int(input())+1
    arr = [x for x in str(n)]
    while len(arr)!= len(set(arr)):
      n+=1
      arr = [x for x in str(n)]
    print(n)

if __name__ == '__main__':
    main()
