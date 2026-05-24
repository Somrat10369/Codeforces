import sys

useless  = sys.stdin.readline()
A = sorted(list(map(int, sys.stdin.readline().strip().split(" "))))
B = sorted(list(map(int, sys.stdin.readline().strip().split(" "))))

print ("yes") if A == B else print("no")
