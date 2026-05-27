import sys

input = lambda: sys.stdin.readline().rstrip("\r\n")
lint = lambda: list(map(int, input().split()))

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

def count_divisors(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i * i != n:
                count += 1
    return count

def solve():
    n_count = input()
    arr = lint()
    if not arr:
        return

    num_max = max(arr)
    num_min = min(arr)
    num_prime = 0
    num_palindrome = 0
    max_divisors_found = 0
    num_max_divisors = arr[0]

    for x in arr:

        if is_prime(x):
            num_prime += 1

        if is_palindrome(x):
            num_palindrome += 1

        current_divisors = count_divisors(x)
        if current_divisors > max_divisors_found:
            max_divisors_found = current_divisors
            num_max_divisors = x
        elif current_divisors == max_divisors_found:
            if x > num_max_divisors:
                num_max_divisors = x

    print(f"The maximum number : {num_max}")
    print(f"The minimum number : {num_min}")
    print(f"The number of prime numbers : {num_prime}")
    print(f"The number of palindrome numbers : {num_palindrome}")
    print(f"The number that has the maximum number of divisors : {num_max_divisors}")


def main():
    sys.setrecursionlimit(200000)
    t = 1
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
