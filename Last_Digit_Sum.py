'''
Given two numbers N and M. Print the summation of their last digits.
Input
Only one line containing two numbers N, M (0 ≤ N, M ≤ 1018).
Output
Print the answer of the problem.
'''

import sys
n , m = sys.stdin.readline().strip().split(" ")
def main(n, m):
  sum_last = int(str(n)[-1]) + int(str(m)[-1])
  print(sum_last)
if __name__ == "__main__":
  main(n,m)

