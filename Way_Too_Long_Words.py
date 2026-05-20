import sys

def main():
  n = int(sys.stdin.readline().strip())

  for _ in range(n):
    word = sys.stdin.readline().strip()
    if len(word) > 10 :
      print (word[0] + str(len(word)-2) + word[-1])
    else:
      print(word)

if __name__ == "__main__":
  main()
