import sys
input  = int(sys.stdin.readline().strip())

year = input // 365
month = (input % 365) // 30
day = input - year * 365 - month * 30

print(f'''{year} years
{month} months
{day} days
''')
