#!/usr/bin/env python3
import subprocess

def solve():
    # The encrypted bytes are located at offset 0x2150 in the binary
    # We can read them directly from the file
    try:
        with open("rev_ironheart_echo/iron", "rb") as f:
            f.seek(0x2150)
            encrypted_bytes = f.read(24)
    except FileNotFoundError:
        print("Error: Binary file 'rev_ironheart_echo/iron' not found.")
        return

    # The decryption logic is XOR with 0x30
    flag = ""
    for b in encrypted_bytes:
        flag += chr(b ^ 0x30)

    print(f"Flag found: {flag}")

    # Verify with the binary
    print("\nVerifying with binary...")
    try:
        p = subprocess.Popen(["./rev_ironheart_echo/iron"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = p.communicate(input=flag + "\n")
        print(stdout)
    except Exception as e:
        print(f"Error running binary: {e}")

if __name__ == "__main__":
    solve()
