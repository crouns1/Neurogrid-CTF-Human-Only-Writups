import sys

def is_repeating_pattern(arr):
    """
    Check if array can be formed by repeating a shorter prefix.
    """
    n = len(arr)
    
    # Try all possible prefix lengths that divide n evenly
    for prefix_len in range(1, n):
        if n % prefix_len == 0:
            # Check if repeating this prefix gives us the full array
            prefix = arr[:prefix_len]
            repetitions = n // prefix_len
            
            if prefix * repetitions == arr:
                return True
    
    return False

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
    
    if is_repeating_pattern(arr):
        print("YES")
    else:
        print("NO")
