import sys, functools,time
input = lambda: sys.stdin.readline().rstrip("\r\n")
def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

# ======================= ignore avobe this line ===================== #

@timer
def solve():
    n = int(eval(input()))
    limit = (n - 1) // 2
    is_prime = bytearray([1]) * (limit + 1)
    counter = 1

    max_i = int(n**0.5) // 2

    for i in range(1, max_i + 1):
        if is_prime[i]:
          p = 2 * i + 1
          start = (p * p - 1) // 2
          for j in range(start, limit + 1, p):
                is_prime[j] = 0

    counter += sum(is_prime)-1
    print(counter)

# --------------------------------------------------------------------- #
# Input (N) | Prime Count | Execution Time |
# ----------|-------------|----------------|
# 10**8     | 5,761,455   | 1.3969 s       |
# 10**7     | 664,579     | 0.0649 s       |
# 10**6     | 78,498      | 0.0043 s       |
# 10**5     | 9,592       | 0.0006 s       |
# 10**4     | 1,229       | 0.0002 s       |
# 10**3     | 168         | 0.0001 s       |
# 10**2     | 25          | 0.0001 s       |
# 10        | 4           | 0.0001 s       |
# -------------------------------------------------------------------- #
# Time complexity O(n log log n)

# ======================= ignore below this line ===================== #


def main():
    sys.setrecursionlimit(200000)
    t = 1
    try:
        t = int(input())
    except ValueError:
        pass
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()

