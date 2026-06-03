import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    n = list((input()).lower())
    vl = ["a","e","i","o","u","y"]
    n = [char for char in n if char not in vl]
    rest = ".".join(n)
    print("."+f"{rest}")


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
