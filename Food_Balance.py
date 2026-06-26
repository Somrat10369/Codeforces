import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def main():
    A, B,C, D  = mint()
    if abs(A-B)==abs(C-D):print("Both")
    else: print("First" if abs(A-B)<abs(C-D) else "Second")

if __name__ == '__main__':
    main()
