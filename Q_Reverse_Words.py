import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
    line = sys.stdin.readline()
    if not line:
        return

    word_chars = []
    first = True

    for char in line:
        if char == ' ' or char == '\n' or char == '\r':
            if word_chars:
                if not first:
                    sys.stdout.write(" ")
                sys.stdout.write("".join(reversed(word_chars)))
                first = False
                word_chars.clear()
        else:
            word_chars.append(char)


    if word_chars:
        if not first:
            sys.stdout.write(" ")
        sys.stdout.write("".join(reversed(word_chars)))

    sys.stdout.write("\n")

def main():
    sys.setrecursionlimit(200000)

    t = 1
    #try:
    #    t = int(input())
    #except ValueError:
    #    pass

    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
