import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    len_n = input()
    a_to_z_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    A = set(input().lower())
    print("YES") if A == a_to_z_set else print("NO")



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
