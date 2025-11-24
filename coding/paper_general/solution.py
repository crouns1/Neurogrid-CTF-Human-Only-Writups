import sys

# Read all input
lines = sys.stdin.read().strip().split('\n')

# First line is the number of test cases
t = int(lines[0])

# Process each test case
for i in range(1, t +1):
    n, k = map(int, lines[i].split())
    print(n * (2 ** k))
