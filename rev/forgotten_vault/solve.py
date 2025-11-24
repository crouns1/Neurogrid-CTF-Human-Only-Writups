import struct

def rol(x, n):
    return ((x << n) | (x >> (16 - n))) & 0xFFFF

def ror(x, n):
    return ((x >> n) | (x << (16 - n))) & 0xFFFF

def solve():
    try:
        with open("rev_forgotten_vault/forgotten_vault", "rb") as f:
            f.seek(0x3080)
            data = f.read(88)
    except FileNotFoundError:
        print("Error: Binary file not found.")
        return

    # Unpack as 44 unsigned shorts (little-endian)
    words = list(struct.unpack("<44H", data))
    
    # The loop goes from i = 43 down to 0
    # prev_byte starts at 0x41
    prev_byte = 0x41
    
    decoded_chars = []
    
    # We need to process in the order the loop does: 43 down to 0
    # But wait, the loop modifies the array in place.
    # And it uses the result of the previous iteration (which was i+1) for the next (i).
    # So we should simulate exactly as the code does.
    
    # Wait, the loop modifies `_[i]`.
    # And `prev_byte` is updated.
    
    # Let's trace the loop:
    # for i in range(43, -1, -1):
    #   val = words[i]
    #   val ^= 0x4d4c
    #   val = rol(val, 2)
    #   val ^= 0x4944
    #   val = ror(val, 5)
    #   val -= prev_byte
    #   val &= 0xffff # Handle underflow if any
    #   
    #   char_code = val & 0xff
    #   prev_byte = char_code
    #   words[i] = val # Not strictly needed for decoding but good for correctness
    #   decoded_chars.append(chr(char_code))
    
    # Since we iterate backwards, the decoded characters will be in reverse order?
    # No, `decoded_chars` will store char at 43, then 42...
    # So we need to reverse the result string.
    
    for i in range(43, -1, -1):
        val = words[i]
        
        # 12c7: xor eax, 0x4d4c
        val ^= 0x4d4c
        
        # 12e9: rol eax, 0x2
        val = rol(val, 2)
        
        # 130d: xor eax, 0x4944
        val ^= 0x4944
        
        # 132f: ror eax, 0x5
        val = ror(val, 5)
        
        # 1357: sub eax, edx (prev_byte)
        val = (val - prev_byte) & 0xFFFF
        
        # 1376: and eax, 0xff
        char_code = val & 0xFF
        
        # 1398: mov [rbp-0x19], al
        prev_byte = char_code
        
        decoded_chars.append(chr(char_code))
        
    # The loop processes index 43 (last char) first, down to 0 (first char).
    # So decoded_chars is [char_43, char_42, ..., char_0]
    # We need to reverse it to get [char_0, ..., char_43]
    
    flag = "".join(decoded_chars[::-1])
    print(f"Flag: {flag}")

if __name__ == "__main__":
    solve()
