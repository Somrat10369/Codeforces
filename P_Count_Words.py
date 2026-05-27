import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(str, input().split(" ")))

def solve():
    n = input()

    count = 0
    in_word = False

    for i in n:
        if i.isalpha():
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False

    print(count)

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
