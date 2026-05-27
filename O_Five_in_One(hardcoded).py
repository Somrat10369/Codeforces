import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

def solve():
  n = input()
  arr = lint()

  num_max = max(arr)
  num_min=min(arr)
  num_prime=0
  num_palindrome =0
  num_max_divisors=0

  prime_nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
  for i in arr:
    if i in prime_nums: num_prime +=1

  palindrome_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]
  for i in arr:
    if i in palindrome_nums: num_palindrome +=1

  max_divisor_nums = [96, 90, 84, 72, 60, 80, 48, 100, 36, 88, 78, 70, 66, 56, 54, 42, 40, 30, 24, 64, 99, 98, 92, 76, 75, 68, 63, 52, 50, 45, 44, 32, 28, 20, 18, 12, 81, 16, 95, 94, 93, 91, 87, 86, 85, 82, 77, 74, 69, 65, 62, 58, 57, 55, 51, 46, 39, 38, 35, 34, 33, 27, 26, 22, 21, 15, 14, 10, 8, 6, 49, 25, 9, 4, 97, 89, 83, 79, 73, 71, 67, 61, 59, 53, 47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2, 1]
  for i in max_divisor_nums:
    if i in arr:
      num_max_divisors = i
      break

  print(f"""The maximum number : {num_max}
The minimum number : {num_min}
The number of prime numbers : {num_prime}
The number of palindrome numbers : {num_palindrome}
The number that has the maximum number of divisors : {num_max_divisors}
        """)


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
