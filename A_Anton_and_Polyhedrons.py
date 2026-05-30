import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split("\n")))

def solve():
  n = int(input())
  output = 0
  dict = {"Tetrahedron":4,
           "Cube":6,
           "Octahedron":8,
           "Dodecahedron":12,
           "Icosahedron":20
           }
  for i in range(n):
    output += dict[str(input())]
  print(output)

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
