import sys
from bisect import bisect_left

def longest_increasing_subsequence(arr):
    """
    Find the length of the longest strictly increasing subsequence.
    Uses binary search approach for O(n log n) complexity.
    """
    if not arr:
        return 0
    
    # tails[i] = smallest ending value of increasing subsequence of length i+1
    tails = []
    
    for num in arr:
        # Binary search for the position to insert/replace
        pos = bisect_left(tails, num)
        
        if pos == len(tails):
            # num is larger than all elements in tails
            tails.append(num)
        else:
            # Replace the element at pos with num
            tails[pos] = num
    
    return len(tails)

# Read all input
lines = sys.stdin.read().strip().split('\n')

# Process pairs of lines (n, then array)
i = 0
while i < len(lines):
    if i >= len(lines):
        break
    
    n = int(lines[i])
    i += 1
    
    if i >= len(lines):
        break
        
    arr = list(map(int, lines[i].split()))
    i += 1
    
    result = longest_increasing_subsequence(arr)
    print(result)
