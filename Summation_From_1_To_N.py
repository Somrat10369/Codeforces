'''
Given a number N
. Print the summation of the numbers that is between 1 and N
 (inclusive).

.∑i=1Ni
Input
Only one line containing a number N
 (1≤N≤109)

Output
Print the summation of the numbers that are between 1 and N
 (inclusive).
'''

import sys

n = int(sys.stdin.readline().strip())

print(int(n*(n+1)//2))
